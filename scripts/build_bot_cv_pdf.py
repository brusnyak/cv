from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "yegor-brusnyak-bot-cv.pdf"

ACCENT = colors.HexColor("#2554e8")
TEXT = colors.HexColor("#15140f")
MUTED = colors.HexColor("#6b6862")
BORDER = colors.HexColor("#d8d5cf")
BG = colors.HexColor("#faf9f7")


def link(url: str, label: str) -> str:
    return f'<link href="{url}"><font color="#2554e8">{label}</font></link>'


def bullet(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(f"&bull; {text}", style)


def build() -> None:
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="Name",
            fontName="Helvetica-Bold",
            fontSize=28,
            leading=30,
            textColor=TEXT,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Role",
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=16,
            textColor=ACCENT,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Meta",
            fontName="Helvetica",
            fontSize=8.7,
            leading=12,
            textColor=MUTED,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=14,
            textColor=ACCENT,
            spaceBefore=12,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            fontName="Helvetica",
            fontSize=9.2,
            leading=13,
            textColor=TEXT,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Small",
            fontName="Helvetica",
            fontSize=8.3,
            leading=11,
            textColor=MUTED,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ProjectTitle",
            fontName="Helvetica-Bold",
            fontSize=10.4,
            leading=13,
            textColor=TEXT,
            spaceBefore=5,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CvBullet",
            fontName="Helvetica",
            fontSize=8.9,
            leading=12.2,
            leftIndent=7,
            firstLineIndent=-7,
            textColor=TEXT,
            spaceAfter=3,
        )
    )

    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(BG)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.setStrokeColor(colors.Color(0.15, 0.33, 0.91, alpha=0.18))
        canvas.setLineWidth(0.4)
        for x, y, r in [(470, 760, 2), (510, 690, 1.2), (70, 120, 1.5), (120, 680, 1)]:
            canvas.circle(x, y, r, fill=0, stroke=1)
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(24 * mm, 13 * mm, "Yegor Brusnyak - Messaging Bot Developer")
        canvas.drawRightString(A4[0] - 24 * mm, 13 * mm, f"Page {doc.page}")
        canvas.restoreState()

    doc = BaseDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="resume", frames=[frame], onPage=on_page)])

    story = []
    story.append(Paragraph("Yegor Brusnyak", styles["Name"]))
    story.append(Paragraph("Messaging Bot Developer", styles["Role"]))
    story.append(
        Paragraph(
            "Bratislava, Slovakia - Remote contract / part-time - English-first<br/>"
            "Email: brusnyakyegor@gmail.com - "
            f"{link('https://github.com/brusnyak', 'github.com/brusnyak')} - "
            f"{link('https://linkedin.com/in/yegor-brusnyak', 'linkedin.com/in/yegor-brusnyak')}<br/>"
            f"Bot proof page: {link('https://brusnyak.github.io/cv/bot/', 'brusnyak.github.io/cv/bot/')} - "
            f"Demo: {link('https://youtu.be/hBkcg5dF5OI', 'youtu.be/hBkcg5dF5OI')}",
            styles["Meta"],
        )
    )

    story.append(Paragraph("Target Fit", styles["Section"]))
    story.append(
        Paragraph(
            "Bot/backend builder focused on Telegram, Discord, Slack, WhatsApp-style webhooks, "
            "dialogue state, LLM fallback, logging, and human-reviewed outbound workflows. Best fit for "
            "roles that need practical messaging-platform integration, bot reliability, and backend API work.",
            styles["Body"],
        )
    )

    proof = [
        ["4", "channel families shown"],
        ["2", "live bot examples"],
        ["5", "runtime smoke suites"],
        ["1", "shared state graph"],
    ]
    table = Table(proof, colWidths=[16 * mm, 43 * mm] * 2)
    table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (-1, -1), TEXT),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("FONTNAME", (2, 0), (2, -1), "Helvetica-Bold"),
                ("TEXTCOLOR", (0, 0), (0, -1), ACCENT),
                ("TEXTCOLOR", (2, 0), (2, -1), ACCENT),
                ("FONTSIZE", (0, 0), (-1, -1), 8.5),
                ("BOX", (0, 0), (-1, -1), 0.4, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.3, BORDER),
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(table)

    story.append(Paragraph("Selected Bot Projects", styles["Section"]))
    projects = [
        (
            "Channel Agent Runtime",
            "Config-driven runtime where Telegram, Discord, Slack, and WhatsApp-style events normalize into one LangGraph state graph for route selection, tool execution, JSONL audit, and approval-first replies.",
            "Node.js, LangGraph, grammY, discord.js, Slack Bolt, webhooks",
            "https://github.com/brusnyak/channel-agent-runtime",
        ),
        (
            "Telegram Salon Bot",
            "Appointment-setting Telegram bot with inline keyboard flow, stylist/service/date/time selection, SQLite-backed bookings, admin commands, reminders, and optional operations webhook events.",
            "Python, Telegram Bot API, SQLite, schedulers, systemd",
            "https://github.com/brusnyak/telegram-salon-bot",
        ),
        (
            "Discord Moderation Bot",
            "Discord bot with slash commands, warning ladder, tickets, auto-moderation, audit logging, SQLite case history, safe demo incidents, and optional LLM moderation assistance.",
            "Python, discord.py, slash commands, SQLite, OpenRouter",
            "https://github.com/brusnyak/discord-mod-bot",
        ),
        (
            "Messaging Bot Ops Lab",
            "Local operations system with provider-shaped webhook intake, persisted conversation state, raw payload visibility, intent/urgency extraction, eval checks, and approval/rejection before outbound replies.",
            "React, Node.js, webhook intake, outbox queue, eval checks",
            "https://github.com/brusnyak/jobiz/tree/main/apps/messaging-bot-ops-lab",
        ),
        (
            "Lingonberry Journal",
            "Trading journal product with Telegram bot commands, web dashboard, analytics, TradeLocker integration, and Telegram Mini App style workflow. Shows bot actions connected to real stored workflow state.",
            "Telegram bot, web dashboard, analytics, TradeLocker, workflow state",
            "https://github.com/brusnyak/lingonberry_journal",
        ),
    ]
    for title, desc, stack, url in projects:
        story.append(Paragraph(title, styles["ProjectTitle"]))
        story.append(Paragraph(desc, styles["Body"]))
        story.append(Paragraph(f"Stack: {stack}<br/>Link: {link(url, url)}", styles["Small"]))

    story.append(PageBreak())
    story.append(Paragraph("Role-Relevant Capabilities", styles["Section"]))
    for item in [
        "Telegram via Bot API and grammY/python-telegram-bot.",
        "Discord via discord.js and discord.py with commands, events, moderation flows, and case history.",
        "Slack via Bolt Socket Mode in the shared runtime.",
        "WhatsApp-style inbound webhooks for Meta/Twilio/Hermes-shaped payloads.",
        "REST/webhook endpoints, OAuth/API integration, async request handling, and deployment handoff.",
        "Conversation state persisted for review and replay using SQLite/JSONL-style workflow proof.",
        "LLM-assisted drafting treated as draft behavior with fallbacks, logs, and human approval gates.",
        "Raw payload visibility and eval checks before risky outbound replies.",
    ]:
        story.append(bullet(item, styles["CvBullet"]))

    story.append(Paragraph("Honest Production Boundary", styles["Section"]))
    story.append(
        Paragraph(
            "Telegram and Discord proof are live-testable bot examples. Slack auth and send checks are validated "
            "in the runtime. WhatsApp work is currently webhook handling and local workflow proof; production sending "
            "requires Meta Cloud API or Twilio sender setup, templates, opt-in rules, and account credentials. "
            "The demos are portfolio proof and implementation evidence, not inflated enterprise client deployments.",
            styles["Body"],
        )
    )

    story.append(Paragraph("General Engineering Background", styles["Section"]))
    for item in [
        "Independent AI engineer and product builder shipping voice agents, LLM applications, and workflow automation.",
        "Experience with Python, FastAPI, Node.js, React/Next.js, PostgreSQL/SQLite, Docker, Vercel, webhooks, and LLM APIs.",
        "Bachelor thesis: Real-Time Speech Translation During Online Conferences. Slovak University of Technology, expected 2027.",
        "Languages: English, German, Ukrainian, Slovak, Russian.",
    ]:
        story.append(bullet(item, styles["CvBullet"]))

    story.append(Spacer(1, 8))
    story.append(
        Paragraph(
            "Primary proof page: "
            f"{link('https://brusnyak.github.io/cv/bot/', 'https://brusnyak.github.io/cv/bot/')}",
            styles["Body"],
        )
    )

    doc.build(story)


if __name__ == "__main__":
    build()
