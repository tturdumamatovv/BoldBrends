from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "BoldBrends Admin",
    "SITE_HEADER": "BoldBrends Admin",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    # "SITE_ICON": {
    #     "light": lambda request: static("icon-light.svg"),  # light mode
    #     "dark": lambda request: static("icon-dark.svg"),  # dark mode
    # },
    # # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    # "SITE_LOGO": {
    #     "light": lambda request: static("logo-light.svg"),  # light mode
    #     "dark": lambda request: static("logo-dark.svg"),  # dark mode
    # },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    # "SITE_FAVICONS": [
    #     {
    #         "rel": "icon",
    #         "sizes": "32x32",
    #         "type": "image/svg+xml",
    #         "href": lambda request: static("favicon.svg"),
    #     },
    # ],
    "SHOW_HISTORY": False,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True,  # show/hide "View on site" button, default: True
    # "ENVIRONMENT": "sample_app.environment_callback",
    # "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
    "LOGIN": {
        "image": lambda request: static("sample/login-bg.jpg"),
      # "redirect_after": lambda request: reverse_lazy("admin:authentication_user_changelist"),
    },
    # "STYLES": [
    #     lambda request: static("css/style.css"),
    # ],
    # "SCRIPTS": [
    #     lambda request: static("js/script.js"),
    # ],
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "255 244 230",
            "100": "255 230 204",
            "200": "255 215 179",
            "300": "255 196 143",
            "400": "255 171 87",
            "500": "255 145 0",
            "600": "234 128 0",
            "700": "202 111 0",
            "800": "171 92 0",
            "900": "140 74 0",
            "950": "112 59 0"
        }
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "ru": "🇷🇺",
                "uz": "🇺🇿",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Отключить поиск в именах приложений и моделей
        "show_all_applications": True,  # Отключить раскрывающееся меню со всеми приложениями и моделями
        "navigation": [
            {
                "title": _("Информация о компании"),
                "icon": "info",
                "collapsible": True,
                "collapsed": True,
                "items": [
                    {
                        "title": _("Информация о компании"),
                        "icon": "info",
                        "link": reverse_lazy("admin:site_info_companyinfo_changelist"),
                    },
                ],
            },
            {
                "title": _("Контент"),
                "icon": "info",
                "collapsible": True,
                "collapsed": True,
                "items": [
                    {
                        "title": _("Баннеры"),
                        "icon": "ad",
                        "link": reverse_lazy("admin:banners_banners_changelist"),
                    },
                    {
                        "title": _("Отделы маркетинга"),
                        "icon": "layers",
                        "link": reverse_lazy("admin:pages_marketingdepartment_changelist"),
                    },
                    {
                        "title": _("Достижения компании"),
                        "icon": "star",
                        "link": reverse_lazy("admin:pages_companyachievements_changelist"),
                    },
                    {
                        "title": _("Проблемы компании"),
                        "icon": "problem",
                        "link": reverse_lazy("admin:pages_companychallenges_changelist"),
                    },
                    {
                        "title": _("Услуги компании"),
                        "icon": "help",
                        "link": reverse_lazy("admin:pages_companyservices_changelist"),
                    },
                    {
                        "title": _("Теги"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:pages_tags_changelist"),
                    },
                    {
                        "title": _("Социальные сети"),
                        "icon": "public",
                        "link": reverse_lazy("admin:pages_socialmedia_changelist"),
                    },
                    {
                        "title": _("Посты компании"),
                        "icon": "post",
                        "link": reverse_lazy("admin:pages_companyposts_changelist"),
                    },
                    {
                        "title": _("Партнеры компании"),
                        "icon": "handshake",
                        "link": reverse_lazy("admin:pages_companypartners_changelist"),
                    },
                    {
                        "title": _("Отзывы партнеров"),
                        "icon": "star",
                        "link": reverse_lazy("admin:pages_partnersreviews_changelist"),
                    },  
                    {
                        "title": _("Заявка на партнерство"),
                        "icon": "star",
                        "link": reverse_lazy("admin:pages_companyapplication_changelist"),
                    },
                    {
                        "title": _("Форма заявки на партнерство"),
                        "icon": "star",
                        "link": reverse_lazy("admin:pages_applicationform_changelist"),
                    },
                    {
                        "title": _("Статические страницы"),
                        "icon": "pages",
                        "link": reverse_lazy("admin:pages_staticpages_changelist"),
                    },
                    {
                        "title": _("Команда компании"),
                        "icon": "group",
                        "link": reverse_lazy("admin:pages_companyteam_changelist"),
                    },
                    {
                        "title": _("Реклама компании"),
                        "icon": "ad",
                        "link": reverse_lazy("admin:pages_companyadvertising_changelist"),
                    },
                    {
                        "title": _("Видеоотзывы от наших клиентов"),
                        "icon": "star",
                        "link": reverse_lazy("admin:pages_companyvideoreviews_changelist"),
                    },
                    {
                        "title": _("Часто задаваемые вопросы"),
                        "icon": "help",
                        "link": reverse_lazy("admin:pages_faq_changelist"),
                    },
                    {
                        "title": _("Брендинг компании"),
                        "icon": "store",
                        "link": reverse_lazy("admin:pages_companybrending_changelist"),
                    },
                    {
                        "title": _("Преимущества компании"),
                        "icon": "list",
                        "link": reverse_lazy("admin:pages_companyfeatures_changelist"),
                    },
                    {
                        "title": _("Видеопродукция"),
                        "icon": "videocam",
                        "link": reverse_lazy("admin:pages_videoproduction_changelist"),
                    },
                    {
                        "title": _("Услуги CRM"),
                        "icon": "list",
                        "link": reverse_lazy("admin:pages_crmservice_changelist"),
                    },
                    {
                        "title": _("Маркетинговая поддержка"),
                        "icon": "shop",
                        "link": reverse_lazy("admin:pages_marketingsupport_changelist"),
                    },
                    {
                        "title": _("Услуги которые мы предлагаем"),
                        "icon": "info",
                        "link": reverse_lazy("admin:pages_serviceoffering_changelist"),
                    },
                    {
                        "title": _("Визитки"),
                        "icon": "card_membership",
                        "link": reverse_lazy("admin:pages_businesscards_changelist"),
                    },
                    {
                        "title": _("Печатные услуги"),
                        "icon": "print",
                        "link": reverse_lazy("admin:pages_printingservice_changelist"),
                    },
                    {
                        "title": _("Дизайн и разработка"),
                        "icon": "design_services",
                        "link": reverse_lazy("admin:pages_designdevelopment_changelist"),
                    },
                ],
            },
            {
                "title": _("Настройки"),
                "icon": "settings",
                "collapsible": True,
                "collapsed": True,
                "items": [
                    {
                        "title": _("Типы бизнеса"),
                        "icon": "business",
                        "link": reverse_lazy("admin:pages_businesstype_changelist"),
                    },
                    {
                        "title": _("Типы продвижения"),
                        "icon": "publish",
                        "link": reverse_lazy("admin:pages_promotiontype_changelist"),
                    },
                    {
                        "title": _("Типы статуса сайта"),
                        "icon": "web",
                        "link": reverse_lazy("admin:pages_sitestatustype_changelist"),
                    },
                    {
                        "title": _("Типы сайта"),
                        "icon": "Share",
                        "link": reverse_lazy("admin:pages_sitetype_changelist"),
                    },
                    {
                        "title": _("Услуги продвижения"),
                        "icon": "sms",
                        "link": reverse_lazy("admin:pages_servicetype_changelist"),
                    },
                    {
                        "title": _("Видео продвижения"),
                        "icon": "pause",
                        "link": reverse_lazy("admin:pages_videotype_changelist"),
                    },
                    {
                        "title": _("Типы задач"),
                        "icon": "book",
                        "link": reverse_lazy("admin:pages_tasktype_changelist"),
                    },
                    {
                        "title": _("Типы соц. сетец"),
                        "icon": "ios",
                        "link": reverse_lazy("admin:pages_socialtype_changelist"),
                    },
                ]
            }    
        ],
    },
    # "TABS": [
    #     {
    #         "models": [
    #             "app_label.model_name_in_lowercase",
    #         ],
    #         "items": [
    #             {
    #                 "title": _("Your custom title"),
    #                 "link": reverse_lazy("admin:app_label_model_name_changelist"),
    #                 "permission": "sample_app.permission_callback",
    #             },
    #         ],
    #     },
    # ],
}