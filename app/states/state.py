import reflex as rx
from typing import TypedDict, List, Dict


class MenuItem(TypedDict):
    id: int
    name: str
    description: str
    price: float
    category: str
    image_url: str


class Service(TypedDict):
    id: int
    name: str
    description: str
    icon: str


class Reservation(TypedDict):
    event_type: str
    num_guests: int
    date: str
    name: str
    email: str
    phone: str


class ContactMessage(TypedDict):
    name: str
    email: str
    message: str


class GlobalState(rx.State):
    company_name: str = "Good Food Traiteur"
    company_description: str = (
        "Votre partenaire gourmand pour tous vos événements. Nous offrons des services traiteur de haute qualité pour particuliers et professionnels, avec des menus personnalisés, des buffets savoureux et des plats à emporter."
    )
    company_values: str = (
        "Qualité, Fraîcheur, Créativité, Service Client."
    )
    contact_email: str = "contact@goodfood.com"
    contact_phone: str = "01 23 45 67 89"
    address: str = "123 Rue de la Gastronomie, 75000 Paris"
    google_maps_embed_url: str = (
        "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2624.991625692246!2d2.292292615674694!3d48.85837007928748!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e66e2964e34e2d%3A0x8ddca9ee380ef7e0!2sEiffel%20Tower!5e0!3m2!1sen!2sfr!4v1620026714536!5m2!1sen!2sfr"
    )
    opening_hours: Dict[str, str] = {
        "Lundi - Vendredi": "9h00 - 18h00",
        "Samedi": "10h00 - 16h00",
        "Dimanche": "Fermé",
    }
    social_media_links: Dict[str, str] = {
        "facebook": "https://facebook.com/goodfood",
        "instagram": "https://instagram.com/goodfood",
        "twitter": "https://twitter.com/goodfood",
    }
    legal_mentions: str = (
        "© 2024 Good Food Traiteur. Tous droits réservés. Mentions Légales."
    )
    services: List[Service] = [
        {
            "id": 1,
            "name": "Buffets Personnalisés",
            "description": "Des buffets variés et adaptés à vos goûts et à votre événement.",
            "icon": "utensils-crossed",
        },
        {
            "id": 2,
            "name": "Plats à Emporter",
            "description": "Savourez nos délicieux plats chez vous, disponibles à la commande.",
            "icon": "shopping-bag",
        },
        {
            "id": 3,
            "name": "Menus sur Mesure",
            "description": "Créons ensemble le menu parfait pour vos réceptions et occasions spéciales.",
            "icon": "edit-3",
        },
        {
            "id": 4,
            "name": "Événements d'Entreprise",
            "description": "Solutions traiteur professionnelles pour séminaires, cocktails et réunions.",
            "icon": "briefcase",
        },
    ]
    menu_items: List[MenuItem] = [
        {
            "id": 1,
            "name": "Salade César Gourmande",
            "description": "Poulet grillé, parmesan, croûtons à l'ail, sauce César maison.",
            "price": 12.5,
            "category": "Entrées",
            "image_url": "/placeholder.svg",
        },
        {
            "id": 2,
            "name": "Velouté de Potimarron",
            "description": "Crème de potimarron, éclats de châtaigne, huile de noisette.",
            "price": 9.0,
            "category": "Entrées",
            "image_url": "/placeholder.svg",
        },
        {
            "id": 3,
            "name": "Filet de Boeuf Rossini",
            "description": "Filet de boeuf, foie gras poêlé, sauce aux truffes, écrasé de pommes de terre.",
            "price": 28.0,
            "category": "Plats",
            "image_url": "/placeholder.svg",
        },
        {
            "id": 4,
            "name": "Risotto aux Cèpes",
            "description": "Riz Arborio crémeux, cèpes frais, parmesan Reggiano.",
            "price": 22.0,
            "category": "Plats",
            "image_url": "/placeholder.svg",
        },
        {
            "id": 5,
            "name": "Pavlova aux Fruits Rouges",
            "description": "Meringue croquante, crème chantilly légère, coulis et fruits rouges frais.",
            "price": 10.5,
            "category": "Desserts",
            "image_url": "/placeholder.svg",
        },
        {
            "id": 6,
            "name": "Moelleux au Chocolat",
            "description": "Cœur coulant chocolat noir, crème anglaise vanillée.",
            "price": 9.5,
            "category": "Desserts",
            "image_url": "/placeholder.svg",
        },
        {
            "id": 7,
            "name": "Assortiment de Fromages Affinés",
            "description": "Sélection de fromages de nos régions, confiture de figues.",
            "price": 14.0,
            "category": "Fromages",
            "image_url": "/placeholder.svg",
        },
    ]
    menu_categories: List[str] = [
        "Toutes",
        "Entrées",
        "Plats",
        "Desserts",
        "Fromages",
    ]
    selected_menu_category: str = "Toutes"
    reservation_form_data: Reservation = {
        "event_type": "",
        "num_guests": 10,
        "date": "",
        "name": "",
        "email": "",
        "phone": "",
    }
    show_reservation_confirmation: bool = False
    contact_form_data: ContactMessage = {
        "name": "",
        "email": "",
        "message": "",
    }
    show_contact_confirmation: bool = False

    @rx.var
    def filtered_menu_items(self) -> List[MenuItem]:
        if self.selected_menu_category == "Toutes":
            return self.menu_items
        return [
            item
            for item in self.menu_items
            if item["category"]
            == self.selected_menu_category
        ]

    @rx.event
    def set_menu_category(self, category: str):
        self.selected_menu_category = category

    @rx.event
    def handle_reservation_form_change(
        self, field_name: str, value: str
    ):
        if field_name == "num_guests":
            try:
                self.reservation_form_data[field_name] = (
                    int(value)
                )
            except ValueError:
                self.reservation_form_data[field_name] = 0
        else:
            self.reservation_form_data[field_name] = value

    @rx.event
    def handle_reservation_submit(self, form_data: dict):
        self.reservation_form_data["event_type"] = (
            form_data.get("event_type", "")
        )
        self.reservation_form_data["num_guests"] = int(
            form_data.get("num_guests", 0)
        )
        self.reservation_form_data["date"] = form_data.get(
            "date", ""
        )
        self.reservation_form_data["name"] = form_data.get(
            "name", ""
        )
        self.reservation_form_data["email"] = form_data.get(
            "email", ""
        )
        self.reservation_form_data["phone"] = form_data.get(
            "phone", ""
        )
        self.show_reservation_confirmation = True

    @rx.event
    def close_reservation_confirmation(self):
        self.show_reservation_confirmation = False
        self.reservation_form_data = {
            "event_type": "",
            "num_guests": 10,
            "date": "",
            "name": "",
            "email": "",
            "phone": "",
        }

    @rx.event
    def handle_contact_form_change(
        self, field_name: str, value: str
    ):
        self.contact_form_data[field_name] = value

    @rx.event
    def handle_contact_submit(self, form_data: dict):
        self.contact_form_data["name"] = form_data.get(
            "name", ""
        )
        self.contact_form_data["email"] = form_data.get(
            "email", ""
        )
        self.contact_form_data["message"] = form_data.get(
            "message", ""
        )
        self.show_contact_confirmation = True
        self.contact_form_data = {
            "name": "",
            "email": "",
            "message": "",
        }

    @rx.event
    def close_contact_confirmation(self):
        self.show_contact_confirmation = False