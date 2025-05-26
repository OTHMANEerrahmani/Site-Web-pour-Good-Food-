import reflex as rx
from app.states.state import GlobalState, Service


def service_card(service: Service) -> rx.Component:
    return rx.el.div(
        rx.icon(
            tag=service["icon"],
            class_name="h-12 w-12 text-amber-600 mb-4",
        ),
        rx.el.h3(
            service["name"],
            class_name="text-xl font-semibold text-stone-800 mb-2",
        ),
        rx.el.p(
            service["description"],
            class_name="text-sm text-stone-600",
        ),
        class_name="bg-white p-6 rounded-xl shadow-md hover:shadow-lg transition-shadow border border-amber-200 flex flex-col items-center text-center",
    )


def services_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Nos Prestations Traiteur",
                class_name="text-3xl md:text-4xl font-bold text-stone-800 mb-12 text-center",
            ),
            rx.el.div(
                rx.foreach(
                    GlobalState.services, service_card
                ),
                class_name="grid md:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-white",
        id="services",
    )