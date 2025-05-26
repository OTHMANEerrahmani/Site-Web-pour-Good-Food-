import reflex as rx
from app.states.state import GlobalState


def about_us_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Notre Savoir-Faire",
                class_name="text-3xl md:text-4xl font-bold text-stone-800 mb-6 text-center",
            ),
            rx.el.p(
                GlobalState.company_description,
                class_name="text-lg text-stone-700 mb-4 text-center max-w-3xl mx-auto",
            ),
            rx.el.p(
                f"Nos valeurs : {GlobalState.company_values}",
                class_name="text-md text-stone-600 font-medium text-center max-w-2xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-amber-50",
    )