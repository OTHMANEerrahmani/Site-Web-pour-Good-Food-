import reflex as rx
from app.states.state import GlobalState


def footer_icon_link(
    icon_name: str, url: str
) -> rx.Component:
    return rx.el.a(
        rx.icon(
            tag=icon_name,
            class_name="h-6 w-6 text-amber-50 hover:text-amber-300 transition-colors",
        ),
        href=url,
        is_external=True,
        target="_blank",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Horaires d'ouverture",
                        class_name="text-lg font-semibold text-amber-50 mb-3",
                    ),
                    rx.foreach(
                        GlobalState.opening_hours.entries(),
                        lambda item: rx.el.p(
                            f"{item[0]}: {item[1]}",
                            class_name="text-sm text-amber-100",
                        ),
                    ),
                    class_name="w-full md:w-1/3 mb-6 md:mb-0",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Contactez-nous",
                        class_name="text-lg font-semibold text-amber-50 mb-3",
                    ),
                    rx.el.p(
                        GlobalState.contact_email,
                        class_name="text-sm text-amber-100",
                    ),
                    rx.el.p(
                        GlobalState.contact_phone,
                        class_name="text-sm text-amber-100",
                    ),
                    rx.el.p(
                        GlobalState.address,
                        class_name="text-sm text-amber-100 mt-2",
                    ),
                    class_name="w-full md:w-1/3 mb-6 md:mb-0",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Suivez-nous",
                        class_name="text-lg font-semibold text-amber-50 mb-3",
                    ),
                    rx.el.div(
                        footer_icon_link(
                            "facebook",
                            GlobalState.social_media_links[
                                "facebook"
                            ],
                        ),
                        footer_icon_link(
                            "instagram",
                            GlobalState.social_media_links[
                                "instagram"
                            ],
                        ),
                        footer_icon_link(
                            "twitter",
                            GlobalState.social_media_links[
                                "twitter"
                            ],
                        ),
                        class_name="flex space-x-4",
                    ),
                    class_name="w-full md:w-1/3",
                ),
                class_name="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8 flex flex-wrap justify-between",
            ),
            rx.el.div(
                rx.el.p(
                    GlobalState.legal_mentions,
                    class_name="text-center text-xs text-amber-200",
                ),
                class_name="py-4 border-t border-amber-700",
            ),
        ),
        class_name="bg-stone-800 text-white",
    )