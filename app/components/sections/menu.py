import reflex as rx
from app.states.state import GlobalState, MenuItem


def menu_item_card(item: MenuItem) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=item["image_url"],
            alt=item["name"],
            class_name="w-full h-48 object-cover rounded-t-lg",
        ),
        rx.el.div(
            rx.el.h3(
                item["name"],
                class_name="text-xl font-semibold text-stone-800 mb-1",
            ),
            rx.el.p(
                item["description"],
                class_name="text-sm text-stone-600 mb-2 h-16 overflow-y-auto",
            ),
            rx.el.div(
                rx.el.span(
                    f"{item['price']:.2f} €",
                    class_name="text-lg font-bold text-amber-600",
                ),
                rx.el.span(
                    item["category"],
                    class_name="text-xs bg-amber-100 text-amber-700 px-2 py-1 rounded-full font-medium",
                ),
                class_name="flex justify-between items-center mt-3",
            ),
            class_name="p-4",
        ),
        class_name="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow border border-amber-200 flex flex-col",
    )


def menu_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Découvrez Notre Menu",
                class_name="text-3xl md:text-4xl font-bold text-stone-800 mb-8 text-center",
            ),
            rx.el.div(
                rx.foreach(
                    GlobalState.menu_categories,
                    lambda category: rx.el.button(
                        category,
                        on_click=lambda: GlobalState.set_menu_category(
                            category
                        ),
                        class_name=rx.cond(
                            GlobalState.selected_menu_category
                            == category,
                            "bg-amber-600 text-white px-4 py-2 rounded-md font-medium transition-colors",
                            "bg-amber-100 text-amber-700 hover:bg-amber-200 px-4 py-2 rounded-md font-medium transition-colors",
                        ),
                    ),
                ),
                class_name="flex flex-wrap justify-center gap-3 mb-10",
            ),
            rx.el.div(
                rx.foreach(
                    GlobalState.filtered_menu_items,
                    menu_item_card,
                ),
                class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-amber-50",
        id="menu",
    )