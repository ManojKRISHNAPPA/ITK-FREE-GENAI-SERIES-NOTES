"""
Generates sample data for the multimodal RAG demo: charts, an AWS architecture diagram,
and a PDF that mixes prose with those figures.

Run:  python generate_samples.py     (needs matplotlib + reportlab)
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless backend: no display needed
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

BASE = Path(__file__).resolve().parent / "data"
IMG_DIR, DOC_DIR = BASE / "images", BASE / "documents"
IMG_DIR.mkdir(parents=True, exist_ok=True)
DOC_DIR.mkdir(parents=True, exist_ok=True)

QUARTERS = ["Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025"]
REVENUE = [12.4, 15.1, 18.7, 24.3]  # USD millions
REGIONS = {"North America": 42, "Europe": 28, "Asia Pacific": 22, "Rest of World": 8}
COSTS = {"Compute": 38, "Storage": 17, "Data Transfer": 12, "Support": 9}  # USD thousands / month


def revenue_chart(path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
    bars = ax.bar(QUARTERS, REVENUE, color="#2E86AB")
    ax.bar_label(bars, fmt="$%.1fM", padding=3)
    ax.set_title("Quarterly Revenue 2025 (USD millions)", fontsize=14, weight="bold")
    ax.set_ylabel("Revenue (USD millions)")
    ax.set_ylim(0, 28)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def region_pie(path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 5), dpi=150)
    ax.pie(REGIONS.values(), labels=REGIONS.keys(), autopct="%1.0f%%", startangle=90,
           colors=["#2E86AB", "#F6AE2D", "#33658A", "#F26419"])
    ax.set_title("Revenue Share by Region, FY2025", fontsize=14, weight="bold")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def cost_chart(path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
    bars = ax.barh(list(COSTS), list(COSTS.values()), color="#F26419")
    ax.bar_label(bars, fmt="$%dK", padding=3)
    ax.set_title("Monthly AWS Cost by Service (USD thousands)", fontsize=14, weight="bold")
    ax.invert_yaxis()
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def aws_architecture(path: Path) -> None:
    """Three-tier web app: Route 53 -> CloudFront -> ALB -> EC2 Auto Scaling -> RDS / S3."""
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=150)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis("off")
    ax.set_title("AWS Three-Tier Web Application Architecture", fontsize=16, weight="bold")

    # VPC boundary groups related resources so the diagram reads like a real AWS drawing.
    ax.add_patch(FancyBboxPatch((3.6, 0.5), 8.1, 5.2, boxstyle="round,pad=0.05",
                                fc="#F4F8FB", ec="#232F3E", lw=2, ls="--"))
    ax.text(3.8, 5.45, "VPC 10.0.0.0/16", fontsize=11, weight="bold", color="#232F3E")

    nodes = {
        "users": (0.2, 2.9, "Users\n(Internet)", "#888888"),
        "r53": (1.9, 4.4, "Route 53\nDNS", "#8C4FFF"),
        "cf": (1.9, 1.4, "CloudFront\nCDN", "#8C4FFF"),
        "alb": (4.3, 2.9, "Application\nLoad Balancer\n(public subnet)", "#ED7100"),
        "ec2a": (6.7, 4.0, "EC2 Auto Scaling\nAZ-a (private)", "#ED7100"),
        "ec2b": (6.7, 1.8, "EC2 Auto Scaling\nAZ-b (private)", "#ED7100"),
        "rds": (9.4, 4.0, "RDS MySQL\nMulti-AZ", "#3B48CC"),
        "s3": (9.4, 1.8, "S3 Bucket\n(static assets)", "#3F8624"),
    }
    w, h = 1.9, 1.0
    for x, y, label, color in nodes.values():
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04", fc=color, ec="none"))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                color="white", fontsize=9, weight="bold")

    def edge(a: str, b: str) -> None:
        xa, ya, *_ = nodes[a]
        xb, yb, *_ = nodes[b]
        ax.add_patch(FancyArrowPatch((xa + w, ya + h / 2) if xb > xa else (xa + w / 2, ya),
                                     (xb, yb + h / 2) if xb > xa else (xb + w / 2, yb + h),
                                     arrowstyle="-|>", mutation_scale=14, color="#232F3E", lw=1.5))

    for a, b in [("users", "r53"), ("users", "cf"), ("r53", "alb"), ("cf", "alb"),
                 ("alb", "ec2a"), ("alb", "ec2b"), ("ec2a", "rds"), ("ec2b", "rds"), ("ec2b", "s3")]:
        edge(a, b)

    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def build_pdf(path: Path, figures: dict[str, Path]) -> None:
    styles = getSampleStyleSheet()
    body = ParagraphStyle("body", parent=styles["BodyText"], fontSize=10.5, leading=15)
    h1, h2 = styles["Heading1"], styles["Heading2"]
    doc = SimpleDocTemplate(str(path), pagesize=A4, title="FY2025 Business and Cloud Review",
                            leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm)

    def fig(key: str, caption: str, width_cm: float = 15):
        img_path = figures[key]
        from PIL import Image as PILImage
        with PILImage.open(img_path) as im:
            ratio = im.height / im.width
        return [Image(str(img_path), width=width_cm * cm, height=width_cm * ratio * cm),
                Paragraph(f"<i>{caption}</i>", body), Spacer(1, 12)]

    s = [Paragraph("FY2025 Business and Cloud Infrastructure Review", h1),
         Paragraph("Executive summary", h2),
         Paragraph("Revenue grew every quarter of 2025, from $12.4M in Q1 to $24.3M in Q4, a total of "
                   "$70.5M for the year. Q4 was the strongest quarter, up 30% over Q3 ($18.7M), driven by "
                   "enterprise renewals and the launch of the analytics add-on. Revenue roughly doubled "
                   "between Q1 and Q4.", body),
         Spacer(1, 8),
         Paragraph("1. Quarterly revenue", h2),
         Paragraph("Figure 1 shows quarterly revenue. Growth was steady: Q2 rose 22% over Q1, Q3 rose 24% "
                   "over Q2, and Q4 rose 30% over Q3. Growth accelerated each quarter.", body)]
    s += fig("revenue", "Figure 1: Quarterly revenue 2025 (USD millions). Q1 $12.4M, Q2 $15.1M, Q3 $18.7M, Q4 $24.3M.")

    s += [Paragraph("2. Revenue by region", h2),
          Paragraph("North America remains the largest market at 42% of revenue, followed by Europe (28%) "
                    "and Asia Pacific (22%). Rest of World contributes 8%. Asia Pacific is the "
                    "fastest-growing region and is the focus of 2026 expansion.", body)]
    s += fig("region", "Figure 2: Revenue share by region, FY2025.", 12)
    s.append(PageBreak())

    s += [Paragraph("3. Cloud architecture", h2),
          Paragraph("The platform runs as a three-tier web application on AWS inside a single VPC "
                    "(10.0.0.0/16). Users resolve the site through <b>Route 53</b>; static content is "
                    "cached by <b>CloudFront</b>. Requests reach an <b>Application Load Balancer</b> in the "
                    "public subnet, which distributes traffic to <b>EC2 Auto Scaling</b> groups running in "
                    "private subnets across two Availability Zones (AZ-a and AZ-b). Application data lives "
                    "in a <b>Multi-AZ RDS MySQL</b> database, and static assets are stored in an "
                    "<b>S3</b> bucket.", body)]
    s += fig("arch", "Figure 3: AWS three-tier architecture: Route 53, CloudFront, ALB, EC2 Auto Scaling, RDS, S3.", 17)
    s += [Paragraph("Security and resilience", h2),
          Paragraph("Security groups allow only HTTPS (443) to the load balancer. The EC2 instances accept "
                    "traffic only from the ALB security group, and the database accepts MySQL (3306) only "
                    "from the application tier. Multi-AZ deployment of EC2 and RDS removes any single "
                    "point of failure.", body)]
    s.append(PageBreak())

    s += [Paragraph("4. Cloud cost", h2),
          Paragraph("Monthly AWS spend totals $76K. Compute is the largest line item at $38K (50%), then "
                    "Storage ($17K), Data Transfer ($12K) and Support ($9K). Reserved Instances and S3 "
                    "lifecycle policies are planned to cut costs by roughly 15%.", body)]
    s += fig("cost", "Figure 4: Monthly AWS cost by service (USD thousands).")

    table = Table([["Quarter", "Revenue (USD M)", "QoQ growth"],
                   ["Q1 2025", "12.4", "-"], ["Q2 2025", "15.1", "+22%"],
                   ["Q3 2025", "18.7", "+24%"], ["Q4 2025", "24.3", "+30%"]], hAlign="LEFT")
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E86AB")),
                               ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                               ("GRID", (0, 0), (-1, -1), 0.5, colors.grey)]))
    s += [Paragraph("Appendix: revenue table", h2), table]
    doc.build(s)


if __name__ == "__main__":
    figs = {"revenue": IMG_DIR / "quarterly_revenue_chart.png",
            "region": IMG_DIR / "revenue_by_region_pie.png",
            "cost": IMG_DIR / "aws_monthly_cost_chart.png",
            "arch": IMG_DIR / "aws_three_tier_architecture.png"}
    revenue_chart(figs["revenue"])
    region_pie(figs["region"])
    cost_chart(figs["cost"])
    aws_architecture(figs["arch"])
    build_pdf(DOC_DIR / "business_cloud_review.pdf", figs)
    print("Generated:", *[p.name for p in figs.values()], "business_cloud_review.pdf")
