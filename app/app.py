import reflex as rx
from app.components.layout import layout
from app.components.sections.home_hero import (
    home_hero_section,
)
from app.components.sections.about_us import (
    about_us_section,
)
from app.components.sections.services import (
    services_section,
)
from app.components.sections.menu import menu_section
from app.components.sections.reservations import (
    reservations_section,
)
from app.components.sections.contact import contact_section
from app.states.state import GlobalState


def index() -> rx.Component:
    return layout(
        rx.el.div(
            home_hero_section(),
            about_us_section(),
            services_section(),
            menu_section(),
            reservations_section(),
            contact_section(),
        )
    )


app = rx.App(
    theme=rx.theme(
        appearance="light", accent_color="amber"
    ),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index,
    title=f"{GlobalState.company_name} - Traiteur d'Exception",
    description=GlobalState.company_description,
    image="/favicon.ico",
)