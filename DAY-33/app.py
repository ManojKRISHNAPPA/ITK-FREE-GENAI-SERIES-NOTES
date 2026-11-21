import os
from collections import defaultdict
from typing import Annotated, Optional, TypedDict

import boto3
from botocore.exceptions import ClientError
import duckdb
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
import streamlit as st


# ==========================================
# Page & Karnataka Pride Theme Setup
# ==========================================
st.set_page_config(
    page_title="S3 Karnataka Pride Agent",
    page_icon="🟡🔴",
    layout="wide",
    initial_sidebar_state="expanded",
)

KARNATAKA_CSS = """
<style>
    /* Main Dark Canvas */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"] {
        background: radial-gradient(circle at top left, #24070D 0%, #120E10 45%, #0D0B0C 100%) !important;
        color: #F7F3E8 !important;
    }

    /* Karnataka Pride Banner */
    .kn-banner {
        background: linear-gradient(125deg, #7A0618 0%, #B80D28 55%, #5E4300 135%);
        border: 2px solid #FFD100;
        border-radius: 14px;
        padding: 1.15rem 1.4rem;
        margin-bottom: 1rem;
        color: #FFFDF7;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45);
    }

    .kn-banner h1 {
        margin: 0;
        font-size: 1.65rem;
        font-weight: 800;
        color: #FFD100;
        letter-spacing: 0.3px;
    }

    .kn-banner p {
        margin: 0.35rem 0 0 0;
        font-size: 0.95rem;
        color: #F7F3E8;
    }

    .kn-badge {
        display: inline-block;
        background-color: #FFD100;
        color: #2B0309;
        font-weight: 800;
        font-size: 0.75rem;
        padding: 0.22rem 0.65rem;
        border-radius: 999px;
        margin-bottom: 0.45rem;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }

    /* Sidebar Dark Theme */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A060A 0%, #11090B 100%) !important;
        border-right: 1px solid rgba(255, 209, 0, 0.28);
    }

    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #F7F3E8 !important;
    }

    /* Inputs inside sidebar & main area */
    [data-testid="stSidebar"] input,
    [data-testid="stSidebar"] select,
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #241418 !important;
        color: #FFFDF7 !important;
        border-color: rgba(255, 209, 0, 0.35) !important;
    }

    /* High-contrast Karnataka Pride Buttons */
    .stButton > button,
    [data-testid="stBaseButton-secondary"],
    [data-testid="stBaseButton-primary"] {
        background: linear-gradient(180deg, #B80D28 0%, #8A061B 100%) !important;
        color: #FFD100 !important;
        border: 1.5px solid #FFD100 !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        transition: all 0.15s ease-in-out;
    }

    .stButton > button *,
    [data-testid="stBaseButton-secondary"] *,
    [data-testid="stBaseButton-primary"] * {
        color: #FFD100 !important;
    }

    .stButton > button:hover,
    [data-testid="stBaseButton-secondary"]:hover,
    [data-testid="stBaseButton-primary"]:hover {
        background: #FFD100 !important;
        color: #24050A !important;
        border-color: #FFD100 !important;
    }

    .stButton > button:hover *,
    [data-testid="stBaseButton-secondary"]:hover *,
    [data-testid="stBaseButton-primary"]:hover * {
        color: #24050A !important;
    }

    /* Chat Message Cards */
    [data-testid="stChatMessage"] {
        border-radius: 12px;
        padding: 0.65rem 0.9rem;
        margin-bottom: 0.6rem;
        border: 1px solid rgba(255, 209, 0, 0.25);
        background-color: #191214 !important;
        color: #F7F3E8 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.28);
    }

    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] span,
    [data-testid="stChatMessage"] code {
        color: #F7F3E8 !important;
    }

    /* Inline code & tool badges */
    [data-testid="stChatMessage"] code {
        background-color: #2B1318 !important;
        color: #FFD100 !important;
        padding: 0.12rem 0.35rem;
        border-radius: 5px;
    }

    /* Expanders for Tool Calls */
    [data-testid="stExpander"] {
        background-color: #140D0F !important;
        border: 1px solid rgba(255, 209, 0, 0.28) !important;
        border-radius: 10px !important;
    }

    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary * {
        color: #FFD100 !important;
    }

    /* High-Contrast Markdown Tables */
    [data-testid="stChatMessage"] table,
    .stMarkdown table {
        width: 100%;
        border-collapse: collapse;
        margin: 0.75rem 0;
        background-color: #161012 !important;
        color: #F7F3E8 !important;
    }

    [data-testid="stChatMessage"] thead th,
    .stMarkdown thead th {
        background-color: #8A061B !important;
        color: #FFD100 !important;
        font-weight: 700 !important;
        padding: 0.6rem 0.75rem !important;
        border: 1px solid rgba(255, 209, 0, 0.35) !important;
        text-align: left !important;
    }

    [data-testid="stChatMessage"] tbody td,
    .stMarkdown tbody td {
        background-color: #1B1316 !important;
        color: #F7F3E8 !important;
        padding: 0.55rem 0.75rem !important;
        border: 1px solid rgba(255, 209, 0, 0.18) !important;
    }

    [data-testid="stChatMessage"] tbody tr:nth-child(even) td,
    .stMarkdown tbody tr:nth-child(even) td {
        background-color: #24161B !important;
        color: #FFFDF7 !important;
    }

    /* Chat Input Dock */
    [data-testid="stChatInput"] textarea,
    [data-testid="stBottom"] > div {
        background-color: #140E10 !important;
        color: #FFFDF7 !important;
        border-color: rgba(255, 209, 0, 0.35) !important;
    }
</style>
"""
st.markdown(KARNATAKA_CSS, unsafe_allow_html=True)


# ==========================================
# AWS & Runtime Credential Helpers
# ==========================================
def build_boto3_session(
    aws_access_key_id: str = "",
    aws_secret_access_key: str = "",
    aws_session_token: str = "",
    aws_region: str = "",
) -> boto3.Session:
    """Build a boto3 Session using sidebar overrides or default credential chain."""
    kwargs = {}
    if aws_access_key_id.strip() and aws_secret_access_key.strip():
        kwargs["aws_access_key_id"] = aws_access_key_id.strip()
        kwargs["aws_secret_access_key"] = aws_secret_access_key.strip()
        if aws_session_token.strip():
            kwargs["aws_session_token"] = aws_session_token.strip()
    if aws_region.strip():
        kwargs["region_name"] = aws_region.strip()
    return boto3.Session(**kwargs)


def get_active_session() -> boto3.Session:
    return build_boto3_session(
        aws_access_key_id=st.session_state.get("aws_access_key", ""),
        aws_secret_access_key=st.session_state.get("aws_secret_key", ""),
        aws_session_token=st.session_state.get("aws_session_token", ""),
        aws_region=st.session_state.get("aws_region", ""),
    )


def get_s3_client(region: Optional[str] = None):
    """Return an S3 client using active session credentials and optional region override."""
    session = get_active_session()
    if region:
        return session.client("s3", region_name=region)
    return session.client("s3")


# ==========================================
# 1. Bucket Management Tools
# ==========================================
@tool
def list_s3_buckets() -> str:
    """List all S3 buckets in the current AWS account along with creation dates."""
    try:
        client = get_s3_client()
        resp = client.list_buckets()
        buckets = resp.get("Buckets", [])
        if not buckets:
            return "No S3 buckets found in this AWS account."

        lines = [f"- {b['Name']} | Created: {b['CreationDate']}" for b in buckets]
        return "\n".join(lines)
    except Exception as e:
        return f"Error listing S3 buckets: {str(e)}"


@tool
def create_s3_bucket(bucket: str, region: Optional[str] = None) -> str:
    """
    Create a new S3 bucket.
    Note: AWS requires LocationConstraint for regions other than us-east-1.
    """
    try:
        session = get_active_session()
        effective_region = region or session.region_name or "us-east-1"
        client = get_s3_client(effective_region)

        if effective_region == "us-east-1":
            client.create_bucket(Bucket=bucket)
        else:
            client.create_bucket(
                Bucket=bucket,
                CreateBucketConfiguration={"LocationConstraint": effective_region},
            )
        return f"Successfully created bucket '{bucket}' in region '{effective_region}'."
    except Exception as e:
        return f"Error creating bucket '{bucket}': {str(e)}"


@tool
def delete_s3_bucket(bucket: str, force_empty: bool = False) -> str:
    """
    Delete an S3 bucket.
    Set force_empty=True to delete all objects (and versions, if versioned) before deleting the bucket.
    """
    try:
        client = get_s3_client()
        if force_empty:
            paginator = client.get_paginator("list_object_versions")
            for page in paginator.paginate(Bucket=bucket):
                to_delete = []
                for v in page.get("Versions", []):
                    to_delete.append({"Key": v["Key"], "VersionId": v["VersionId"]})
                for dm in page.get("DeleteMarkers", []):
                    to_delete.append({"Key": dm["Key"], "VersionId": dm["VersionId"]})
                if to_delete:
                    client.delete_objects(
                        Bucket=bucket, Delete={"Objects": to_delete}
                    )

            obj_paginator = client.get_paginator("list_objects_v2")
            for page in obj_paginator.paginate(Bucket=bucket):
                objs = [{"Key": o["Key"]} for o in page.get("Contents", [])]
                if objs:
                    client.delete_objects(Bucket=bucket, Delete={"Objects": objs})

        client.delete_bucket(Bucket=bucket)
        return f"Successfully deleted bucket '{bucket}'."
    except Exception as e:
        return (
            f"Error deleting bucket '{bucket}': {str(e)}. "
            "If the bucket is not empty, retry with force_empty=True."
        )


# ==========================================
# 2. Bucket Analysis Tool
# ==========================================
@tool
def analyze_s3_bucket(
    bucket: str, prefix: str = "", max_objects_to_scan: int = 5000
) -> str:
    """
    Analyze an S3 bucket (or prefix): total object count, total size, file type breakdown,
    top largest files, and configuration (versioning, encryption, public access block).
    """
    try:
        client = get_s3_client()
        paginator = client.get_paginator("list_objects_v2")
        total_objects = 0
        total_bytes = 0
        ext_stats = defaultdict(lambda: {"count": 0, "bytes": 0})
        largest_files = []
        truncated_scan = False

        for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                if total_objects >= max_objects_to_scan:
                    truncated_scan = True
                    break
                total_objects += 1
                size = obj["Size"]
                key = obj["Key"]
                total_bytes += size

                filename = key.split("/")[-1]
                ext = (
                    f".{filename.split('.')[-1].lower()}"
                    if "." in filename and not filename.startswith(".")
                    else "<no_ext>"
                )
                ext_stats[ext]["count"] += 1
                ext_stats[ext]["bytes"] += size
                largest_files.append((size, key))

            if truncated_scan:
                break

        largest_files.sort(key=lambda x: x[0], reverse=True)
        top_5 = (
            "\n".join(
                f"  - {k} ({s / (1024 * 1024):.2f} MB)" for s, k in largest_files[:5]
            )
            or "  - None"
        )

        ext_lines = (
            "\n".join(
                f"  - {ext}: {stats['count']} files ({stats['bytes'] / (1024 * 1024):.2f} MB)"
                for ext, stats in sorted(
                    ext_stats.items(), key=lambda item: item[1]["bytes"], reverse=True
                )
            )
            or "  - None"
        )

        try:
            loc = (
                client.get_bucket_location(Bucket=bucket).get("LocationConstraint")
                or "us-east-1"
            )
        except ClientError:
            loc = "unknown"

        try:
            ver = client.get_bucket_versioning(Bucket=bucket).get("Status", "Disabled")
        except ClientError:
            ver = "unknown"

        try:
            enc_rules = client.get_bucket_encryption(Bucket=bucket)[
                "ServerSideEncryptionConfiguration"
            ]["Rules"]
            enc = ", ".join(
                r["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"]
                for r in enc_rules
            )
        except ClientError:
            enc = "None/Default"

        try:
            pab = client.get_public_access_block(Bucket=bucket)[
                "PublicAccessBlockConfiguration"
            ]
            pab_summary = (
                f"BlockPublicAcls={pab.get('BlockPublicAcls')}, "
                f"BlockPublicPolicy={pab.get('BlockPublicPolicy')}"
            )
        except ClientError:
            pab_summary = "Not configured / restricted"

        scan_note = (
            f" (capped at {max_objects_to_scan} objects)" if truncated_scan else ""
        )

        return (
            f"Bucket Analysis for s3://{bucket}/{prefix}{scan_note}\n"
            f"- Region: {loc}\n"
            f"- Versioning: {ver}\n"
            f"- Encryption: {enc}\n"
            f"- Public Access Block: {pab_summary}\n"
            f"- Objects Scanned: {total_objects}\n"
            f"- Total Size: {total_bytes / (1024 * 1024):.2f} MB ({total_bytes / (1024 ** 3):.3f} GB)\n"
            f"- Breakdown by Extension:\n{ext_lines}\n"
            f"- Largest Files:\n{top_5}"
        )
    except Exception as e:
        return f"Error analyzing bucket '{bucket}': {str(e)}"


# ==========================================
# 3. Object Inspection, Query & Mutation Tools
# ==========================================
@tool
def list_s3_objects(bucket: str, prefix: str = "", max_keys: int = 50) -> str:
    """List files (keys), sizes, and last-modified timestamps in an S3 bucket/prefix."""
    try:
        client = get_s3_client()
        response = client.list_objects_v2(
            Bucket=bucket, Prefix=prefix, MaxKeys=max_keys
        )
        contents = response.get("Contents", [])
        if not contents:
            return f"No objects found in s3://{bucket}/{prefix}"

        lines = [
            f"- {obj['Key']} | Size: {obj['Size'] / 1024:.2f} KB | Modified: {obj['LastModified']}"
            for obj in contents
        ]
        return "\n".join(lines)
    except Exception as e:
        return f"Error listing S3 objects: {str(e)}"


@tool
def inspect_s3_file_preview(bucket: str, key: str, num_bytes: int = 4096) -> str:
    """Read the first few KB of a text/CSV/JSON/log file from S3 to inspect its schema or structure."""
    try:
        client = get_s3_client()
        response = client.get_object(
            Bucket=bucket, Key=key, Range=f"bytes=0-{num_bytes - 1}"
        )
        data = response["Body"].read().decode("utf-8", errors="replace")
        return f"Preview of s3://{bucket}/{key} (first {num_bytes} bytes):\n\n{data}"
    except Exception as e:
        return f"Error previewing file: {str(e)}"


@tool
def upload_s3_object(
    bucket: str,
    key: str,
    content: Optional[str] = None,
    local_path: Optional[str] = None,
) -> str:
    """
    Upload either inline text `content` or a `local_path` file to s3://{bucket}/{key}.
    Provide either `content` or `local_path`.
    """
    try:
        client = get_s3_client()
        if local_path:
            client.upload_file(local_path, bucket, key)
            return f"Uploaded local file '{local_path}' to s3://{bucket}/{key}."
        if content is not None:
            client.put_object(Bucket=bucket, Key=key, Body=content.encode("utf-8"))
            return f"Uploaded text content ({len(content)} chars) to s3://{bucket}/{key}."
        return "Error: Provide either `content` or `local_path`."
    except Exception as e:
        return f"Error uploading to s3://{bucket}/{key}: {str(e)}"


@tool
def delete_s3_object(bucket: str, key: str) -> str:
    """Delete a single object at s3://{bucket}/{key}."""
    try:
        client = get_s3_client()
        client.delete_object(Bucket=bucket, Key=key)
        return f"Deleted s3://{bucket}/{key}."
    except Exception as e:
        return f"Error deleting s3://{bucket}/{key}: {str(e)}"


@tool
def query_s3_with_sql(sql_query: str) -> str:
    """
    Execute a DuckDB SQL query directly against S3 CSV, Parquet, or JSON files.
    Example query: SELECT category, COUNT(*), AVG(price) FROM 's3://my-bucket/sales.parquet' GROUP BY 1 LIMIT 20;
    Always use LIMIT to keep output concise.
    """
    try:
        con = duckdb.connect(database=":memory:")
        con.execute("INSTALL httpfs; LOAD httpfs;")
        session = get_active_session()
        creds = session.get_credentials()
        if creds is None:
            return "SQL Execution Error: No AWS credentials found."
        frozen = creds.get_frozen_credentials()
        region = session.region_name or "us-east-1"

        token_clause = f", SESSION_TOKEN '{frozen.token}'" if frozen.token else ""
        con.execute(
            f"""
            CREATE SECRET (
                TYPE S3,
                KEY_ID '{frozen.access_key}',
                SECRET '{frozen.secret_key}',
                REGION '{region}'
                {token_clause}
            );
            """
        )
        df = con.execute(sql_query).df()
        if len(df) > 100:
            return (
                f"Showing top 100 of {len(df)} rows:\n"
                + df.head(100).to_markdown(index=False)
            )
        return df.to_markdown(index=False)
    except Exception as e:
        return f"SQL Execution Error: {str(e)}"


# ==========================================
# 4. LangGraph Agent Builder
# ==========================================
TOOLS = [
    list_s3_buckets,
    create_s3_bucket,
    delete_s3_bucket,
    analyze_s3_bucket,
    list_s3_objects,
    inspect_s3_file_preview,
    upload_s3_object,
    delete_s3_object,
    query_s3_with_sql,
]
TOOLS_BY_NAME = {t.name: t for t in TOOLS}


class GraphSchema(TypedDict):
    messages: Annotated[list, add_messages]


SYSTEM_PROMPT = """
You are an AWS S3 data and bucket assistant with a warm, crisp, Karnataka Pride spirit.

Use the provided S3 tools to:
- Inspect S3 buckets
- Create and delete buckets
- Analyze bucket contents
- List S3 objects
- Preview files
- Upload and delete objects
- Query CSV, JSON, and Parquet files using SQL.

Guidelines:
- Confirm destructive actions (such as deleting buckets or objects) clearly with the user before executing unless the user explicitly confirmed them.
- Always keep SQL queries bounded with LIMIT.
- Format responses clearly using headings, tables, and bullet points when helpful.
"""


def build_s3_graph(model_name: str, api_key: str, temperature: float = 0.1):
    llm = ChatOpenAI(
        model=model_name,
        api_key=api_key or os.getenv("OPENAI_API_KEY"),
        temperature=temperature,
    )
    llm_with_tools = llm.bind_tools(TOOLS)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    chain = prompt | llm_with_tools

    def llm_node(state: GraphSchema) -> GraphSchema:
        response = chain.invoke({"messages": state["messages"]})
        return {"messages": [response]}

    def tool_node(state: GraphSchema) -> GraphSchema:
        last_msg = state["messages"][-1]
        tool_results = []
        for call in getattr(last_msg, "tool_calls", []):
            tool_fn = TOOLS_BY_NAME.get(call["name"])
            if tool_fn is None:
                obs = f"Error: Unknown tool '{call['name']}'."
            else:
                obs = tool_fn.invoke(call["args"])
            tool_results.append(
                ToolMessage(content=str(obs), tool_call_id=call["id"])
            )
        return {"messages": tool_results}

    def route_after_llm(state: GraphSchema) -> str:
        last_msg = state["messages"][-1]
        if getattr(last_msg, "tool_calls", None):
            return "tool_node"
        return END

    builder = StateGraph(GraphSchema)
    builder.add_node("llm_node", llm_node)
    builder.add_node("tool_node", tool_node)
    builder.add_edge(START, "llm_node")
    builder.add_conditional_edges(
        "llm_node",
        route_after_llm,
        {"tool_node": "tool_node", END: END},
    )
    builder.add_edge("tool_node", "llm_node")
    return builder.compile()


# ==========================================
# Session State Initialization
# ==========================================
if "lc_messages" not in st.session_state:
    st.session_state.lc_messages = []
if "ui_history" not in st.session_state:
    # List of dicts: {"role": "user" | "assistant", "content": str, "tool_steps": list[dict]}
    st.session_state.ui_history = []
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None


# ==========================================
# Sidebar Controls
# ==========================================
with st.sidebar:
    st.markdown("### 🟡🔴 Karnataka Pride Config")

    openai_key_input = st.text_input(
        "OpenAI API Key",
        value=os.getenv("OPENAI_API_KEY", ""),
        type="password",
        help="Falls back to OPENAI_API_KEY environment variable if left blank.",
    )
    model_name = st.selectbox(
        "Model",
        options=["gpt-4o-mini", "gpt-4o", "gpt-4.1-mini"],
        index=0,
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.1, 0.1)

    st.divider()
    st.markdown("### ☁️ AWS Credentials (Optional Override)")
    st.caption("Leave blank to use default AWS credential chain (~/.aws, IAM role, env).")
    st.session_state.aws_access_key = st.text_input(
        "AWS Access Key ID",
        value=st.session_state.get("aws_access_key", os.getenv("AWS_ACCESS_KEY_ID", "")),
        type="password",
    )
    st.session_state.aws_secret_key = st.text_input(
        "AWS Secret Access Key",
        value=st.session_state.get(
            "aws_secret_key", os.getenv("AWS_SECRET_ACCESS_KEY", "")
        ),
        type="password",
    )
    st.session_state.aws_session_token = st.text_input(
        "AWS Session Token",
        value=st.session_state.get(
            "aws_session_token", os.getenv("AWS_SESSION_TOKEN", "")
        ),
        type="password",
    )
    st.session_state.aws_region = st.text_input(
        "Default AWS Region",
        value=st.session_state.get(
            "aws_region", os.getenv("AWS_DEFAULT_REGION", "ap-south-1")
        ),
    )

    st.divider()
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.lc_messages = []
            st.session_state.ui_history = []
            st.session_state.pending_prompt = None
            st.rerun()
    with col_b:
        if st.button("🔌 Test AWS", use_container_width=True):
            try:
                buckets = get_s3_client().list_buckets().get("Buckets", [])
                st.success(f"Connected! {len(buckets)} bucket(s).")
            except Exception as exc:
                st.error(f"AWS error: {exc}")


# ==========================================
# Main Header & Quick Actions
# ==========================================
st.markdown(
    """
    <div class="kn-banner">
        <div class="kn-badge">🟡🔴 Namma S3 Agent • Karnataka Pride Edition</div>
        <h1>AWS S3 Bucket & Data Intelligence Chatbot</h1>
        <p>Inspect buckets, audit encryption & versioning, preview files, upload/delete objects, and query Parquet/CSV/JSON with DuckDB SQL.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

quick_prompts = [
    ("📦 List All Buckets", "List all S3 buckets in my AWS account with their creation dates."),
    ("🔬 Audit a Bucket", "Analyze my primary S3 bucket: total size, file extensions, largest files, versioning, encryption, and public access settings."),
    ("📊 SQL on S3 Data", "Show me an example DuckDB SQL query with LIMIT to inspect Parquet or CSV files in S3."),
    ("📤 Upload Sample Note", "Help me upload a sample text note to an S3 bucket."),
]

q_cols = st.columns(len(quick_prompts))
for idx, (btn_label, prompt_text) in enumerate(quick_prompts):
    with q_cols[idx]:
        if st.button(btn_label, key=f"quick_{idx}", use_container_width=True):
            st.session_state.pending_prompt = prompt_text


# ==========================================
# Render Conversation History
# ==========================================
for turn in st.session_state.ui_history:
    with st.chat_message(turn["role"]):
        if turn.get("tool_steps"):
            for step in turn["tool_steps"]:
                with st.expander(f"🛠️ Tool: `{step['name']}`", expanded=False):
                    st.markdown("**Arguments:**")
                    st.json(step["args"])
                    st.markdown("**Output:**")
                    st.code(step["output"], language="text")
        st.markdown(turn["content"])


# ==========================================
# Handle New Prompt Execution
# ==========================================
user_input = st.chat_input("Ask me to list buckets, analyze storage, preview files, or run S3 SQL...")
if st.session_state.pending_prompt and not user_input:
    user_input = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

if user_input:
    effective_openai_key = openai_key_input or os.getenv("OPENAI_API_KEY", "")
    if not effective_openai_key:
        st.error("Please enter your OpenAI API Key in the sidebar or set `OPENAI_API_KEY`.")
        st.stop()

    # Append user turn
    st.session_state.ui_history.append(
        {"role": "user", "content": user_input, "tool_steps": []}
    )
    st.session_state.lc_messages.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    # Run LangGraph with full conversation history
    graph_app = build_s3_graph(
        model_name=model_name,
        api_key=effective_openai_key,
        temperature=temperature,
    )

    with st.chat_message("assistant"):
        status_placeholder = st.empty()
        tool_steps_collected = []
        pending_calls_by_id = {}
        final_answer = ""

        with st.spinner("Analyzing S3 with LangGraph agent..."):
            for chunk in graph_app.stream(
                {"messages": st.session_state.lc_messages},
                stream_mode="updates",
            ):
                if "llm_node" in chunk:
                    msg = chunk["llm_node"]["messages"][-1]
                    if getattr(msg, "tool_calls", None):
                        for tc in msg.tool_calls:
                            pending_calls_by_id[tc["id"]] = {
                                "name": tc["name"],
                                "args": tc["args"],
                            }
                            status_placeholder.info(f"Running tool `{tc['name']}`...")
                    elif isinstance(msg, AIMessage) and msg.content:
                        final_answer = msg.content

                if "tool_node" in chunk:
                    for tmsg in chunk["tool_node"]["messages"]:
                        if isinstance(tmsg, ToolMessage):
                            meta = pending_calls_by_id.get(
                                tmsg.tool_call_id,
                                {"name": "s3_tool", "args": {}},
                            )
                            step_record = {
                                "name": meta["name"],
                                "args": meta["args"],
                                "output": tmsg.content,
                            }
                            tool_steps_collected.append(step_record)
                            with st.expander(
                                f"🛠️ Tool: `{step_record['name']}`", expanded=False
                            ):
                                st.markdown("**Arguments:**")
                                st.json(step_record["args"])
                                st.markdown("**Output:**")
                                st.code(step_record["output"], language="text")

        status_placeholder.empty()
        if not final_answer:
            final_answer = "Done."
        st.markdown(final_answer)

    # Persist updated history
    st.session_state.lc_messages.append(AIMessage(content=final_answer))
    st.session_state.ui_history.append(
        {
            "role": "assistant",
            "content": final_answer,
            "tool_steps": tool_steps_collected,
        }
    )