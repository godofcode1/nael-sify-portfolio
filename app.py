from flask import Flask, render_template

app = Flask(__name__)

MY_PROJECTS = [
    {
        "id": "001",
        "title": "Maison Noura Restaurant",
        "desc": "A refined restaurant website concept with menu highlights, reservation flow, location details, and a warm visual direction built for trust and appetite.",
        "tags": ["Restaurant", "Booking", "Responsive"],
        "live_url": "https://godofcode1.github.io/maison-noura-restaurant/",
        "repo_url": "https://github.com/godofcode1/maison-noura-restaurant"
    },
    {
        "id": "002",
        "title": "Noir Atelier Clothing",
        "desc": "A fictional clothing brand storefront with editorial product sections, collection storytelling, product cards, and a clean premium fashion feel.",
        "tags": ["Fashion", "E-commerce", "Branding"],
        "live_url": "https://godofcode1.github.io/noir-atelier-clothing/",
        "repo_url": "https://github.com/godofcode1/noir-atelier-clothing"
    },
    {
        "id": "003",
        "title": "Luma Studio Portfolio",
        "desc": "A creative studio website focused on strong first impressions, case-study previews, service blocks, and a polished contact path.",
        "tags": ["Agency", "Portfolio", "UI Design"],
        "live_url": "https://godofcode1.github.io/luma-studio-portfolio/",
        "repo_url": "https://github.com/godofcode1/luma-studio-portfolio"
    },
    {
        "id": "004",
        "title": "CasaStay Rentals",
        "desc": "A modern accommodation website concept with featured stays, neighborhood filters, clear pricing sections, and mobile-first browsing.",
        "tags": ["Travel", "Listings", "UX"],
        "live_url": "https://godofcode1.github.io/casastay-rentals/",
        "repo_url": "https://github.com/godofcode1/casastay-rentals"
    },
    {
        "id": "005",
        "title": "Sable & Steam Cafe",
        "desc": "A coffee and patisserie concept with signature drinks, pastry showcases, daily rhythm, and a warm boutique identity designed to feel premium and inviting.",
        "tags": ["Coffee", "Patisserie", "Branding"],
        "live_url": "https://godofcode1.github.io/sable-and-steam-cafe/",
        "repo_url": "https://github.com/godofcode1/sable-and-steam-cafe"
    },
    {
        "id": "006",
        "title": "Atelier Du Feu",
        "desc": "A restaurant landing page built around chef storytelling, reservation conversion, tasting menus, and a richer editorial presentation for hospitality brands.",
        "tags": ["Restaurant", "Fine Dining", "Editorial"],
        "live_url": "https://godofcode1.github.io/atelier-du-feu/",
        "repo_url": "https://github.com/godofcode1/atelier-du-feu"
    }
]

STATS = [
    {"value": "6", "label": "featured website concepts"},
    {"value": "4", "label": "core skill areas"},
    {"value": "2026", "label": "current portfolio refresh"}
]

SERVICES = [
    {
        "title": "Web Applications",
        "desc": "Front-end and back-end development for fast, responsive, and maintainable products."
    },
    {
        "title": "Automation",
        "desc": "Scripts and internal tools that save time, reduce manual work, and make data easier to use."
    },
    {
        "title": "Interface Design",
        "desc": "Clean layouts, visual direction, and user flows that make technical products easier to understand."
    }
]

@app.route('/')
def home():
    return render_template(
        'index.html',
        projects=MY_PROJECTS,
        stats=STATS,
        services=SERVICES
    )

if __name__ == '__main__':
    app.run(debug=True)
