import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


def layout(main_content: rx.Component) -> rx.Component:
    return rx.el.main(
        navbar(),
        rx.el.div(main_content, class_name="pt-16"),
        footer(),
        class_name="font-['Inter'] bg-white",
    )