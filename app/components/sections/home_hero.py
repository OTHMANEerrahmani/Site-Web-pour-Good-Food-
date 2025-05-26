import reflex as rx
from app.states.state import GlobalState


def home_hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                GlobalState.company_name,
                class_name="text-5xl md:text-7xl font-bold text-white mb-6 text-center shadow-lg",
            ),
            rx.el.p(
                "L'élégance et la saveur pour tous vos événements.",
                class_name="text-xl md:text-2xl text-amber-50 mb-8 text-center shadow-md",
            ),
            rx.el.a(
                rx.el.button(
                    "Découvrir Nos Menus",
                    rx.icon(
                        tag="arrow-right",
                        class_name="ml-2 h-5 w-5",
                    ),
                    class_name="bg-amber-500 hover:bg-amber-600 text-stone-800 font-semibold py-3 px-8 rounded-lg text-lg transition-colors shadow-md hover:shadow-lg flex items-center",
                ),
                href="#menu",
            ),
            class_name="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center justify-center min-h-[calc(100vh-4rem)]",
        ),
        style={
            "background_image": "url('/catering_hero.jpg')",
            "background_size": "cover",
            "background_position": "center",
            "background_attachment": "fixed",
        },
        class_name="relative text-white",
    )