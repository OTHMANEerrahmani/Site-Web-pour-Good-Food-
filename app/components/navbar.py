import reflex as rx
from app.states.state import GlobalState


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        class_name="text-sm font-medium text-white hover:text-amber-300 transition-colors px-3 py-2 rounded-md",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon(
                        tag="chef-hat",
                        class_name="h-8 w-8 mr-2 text-amber-400",
                    ),
                    rx.el.span(
                        GlobalState.company_name,
                        class_name="font-bold text-xl text-white",
                    ),
                    href="/",
                    class_name="flex items-center",
                ),
                rx.el.div(
                    navbar_link("Accueil", "/"),
                    navbar_link(
                        "Nos Services", "#services"
                    ),
                    navbar_link("Menu", "#menu"),
                    navbar_link(
                        "Réserver", "#reservations"
                    ),
                    navbar_link("Contact", "#contact"),
                    class_name="hidden md:flex items-center space-x-1",
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16",
        ),
        class_name="bg-stone-800 shadow-md fixed top-0 left-0 right-0 z-50",
    )