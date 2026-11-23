"""Arabic labels and direction for the Django administration interface."""

from django.contrib.admin import AdminSite
from django.contrib.admin.apps import AdminConfig
from django.contrib.admin.views.main import ChangeList
from django.utils.translation import override


SECTIONS = {
    "apps": "التطبيقات",
    "categories": "التصنيفات",
    "developers": "المطوّرون",
    "metadata": "البيانات الوصفية",
    "submissions": "طلبات إضافة التطبيقات",
    "assistant": "المساعد",
}

MODELS = {
    ("apps", "app"): ("تطبيق", "التطبيقات"),
    ("apps", "appcrawleddata"): ("بيانات المتاجر", "بيانات المتاجر"),
    ("categories", "category"): ("تصنيف", "التصنيفات"),
    ("developers", "developer"): ("مطوّر", "المطوّرون"),
    ("metadata", "metadatatype"): ("نوع بيانات وصفية", "أنواع البيانات الوصفية"),
    ("metadata", "metadataoption"): ("خيار وصفي", "الخيارات الوصفية"),
    ("metadata", "appmetadatavalue"): ("قيمة وصفية", "القيم الوصفية للتطبيقات"),
    ("submissions", "appsubmission"): ("طلب إضافة تطبيق", "طلبات إضافة التطبيقات"),
    ("submissions", "submissionstatuslog"): ("سجل حالة", "سجلات الحالات"),
    ("assistant", "assistantconversation"): ("محادثة", "محادثات المساعد"),
}

HEADINGS = {
    "Basic Information": "المعلومات الأساسية",
    "Descriptions": "الأوصاف",
    "Media": "الصور والوسائط",
    "Legacy Screenshots (JSON)": "لقطات الشاشة القديمة (JSON)",
    "Store Links": "روابط المتاجر",
    "Ratings & Statistics": "التقييمات والإحصاءات",
    "Organization": "التصنيف والمطوّر",
    "Timestamps": "التواريخ",
    "AI Search": "البحث بالذكاء الاصطناعي",
    "Source Information": "معلومات المصدر",
    "Content": "المحتوى",
    "Metadata": "البيانات الوصفية",
    "Visual": "المظهر",
    "Contact Information": "معلومات التواصل",
    "Media & Social": "الوسائط وروابط التواصل",
    "Settings": "الإعدادات",
    "Display": "العرض",
    "Tracking & Status": "التتبّع والحالة",
    "App Details (English)": "بيانات التطبيق بالإنجليزية",
    "App Details (Arabic)": "بيانات التطبيق بالعربية",
    "Categories": "التصنيفات",
    "Developer Information": "معلومات المطوّر",
    "Additional Information": "معلومات إضافية",
    "Review": "المراجعة",
}

FIELDS = {
    "id": "المعرّف", "slug": "المعرّف في الرابط", "status": "الحالة",
    "platform": "المنصة", "featured": "تطبيق مميّز", "is_active": "نشط",
    "is_verified": "مطوّر موثّق", "developer": "المطوّر", "categories": "التصنيفات",
    "application_icon": "أيقونة التطبيق", "google_play_link": "رابط Google Play",
    "app_store_link": "رابط App Store", "app_gallery_link": "رابط AppGallery",
    "avg_rating": "متوسط التقييم", "review_count": "عدد التقييمات",
    "view_count": "عدد المشاهدات", "sort_order": "ترتيب العرض",
    "email": "البريد الإلكتروني", "website": "الموقع الإلكتروني",
    "contact_info": "معلومات التواصل", "logo_url": "رابط الشعار",
    "social_links": "روابط التواصل الاجتماعي", "icon": "الأيقونة",
    "color": "اللون", "language": "اللغة", "image": "الصورة",
    "created_at": "تاريخ الإنشاء", "updated_at": "آخر تحديث",
    "app": "التطبيق", "source": "المصدر", "url": "الرابط",
    "content": "المحتوى", "metadata": "البيانات الوصفية",
    "crawled_at": "تاريخ جلب البيانات", "metadata_type": "نوع البيانات الوصفية",
    "metadata_option": "الخيار الوصفي", "parent": "العنصر الأب",
    "value": "القيمة", "key": "المفتاح", "tracking_id": "رقم التتبّع",
    "submitter_name": "اسم مقدّم الطلب", "submitter_email": "بريد مقدّم الطلب",
    "submitter_phone": "هاتف مقدّم الطلب", "submitter_organization": "جهة مقدّم الطلب",
    "developer_website": "موقع المطوّر", "website_link": "رابط الموقع الإلكتروني",
    "developer_email": "بريد المطوّر", "is_developer": "مقدّم الطلب هو المطوّر",
    "additional_notes": "ملاحظات إضافية", "review_notes": "ملاحظات المراجعة",
    "reviewed_at": "تاريخ المراجعة", "reviewed_by": "المراجِع",
    "rejection_reason": "سبب الرفض", "changed_by": "عدّل بواسطة",
    "old_status": "الحالة السابقة", "new_status": "الحالة الجديدة",
    "notes": "الملاحظات", "conversation_id": "معرّف المحادثة",
}

LANGUAGE_FIELDS = {
    "name": "الاسم", "app_name": "اسم التطبيق", "developer_name": "اسم المطوّر",
    "label": "التسمية", "short_description": "الوصف المختصر", "description": "الوصف",
    "main_image": "صورة الغلاف", "screenshots": "لقطات الشاشة",
}
for code, language in {"ar": "بالعربية", "en": "بالإنجليزية", "ur": "بالأردية"}.items():
    for field, title in LANGUAGE_FIELDS.items():
        FIELDS[f"{field}_{code}"] = f"{title} {language}"

CHOICES = {
    "draft": "مسودة", "published": "منشور", "archived": "مؤرشف",
    "web": "الويب", "cross_platform": "متعدد المنصات",
    "ar": "العربية", "en": "الإنجليزية", "ur": "الأردية",
    "pending": "بانتظار المراجعة", "approved": "مقبول", "rejected": "مرفوض",
    "under_review": "قيد المراجعة", "info_requested": "معلومات مطلوبة",
    "success": "ناجح", "failed": "فشل",
}


class AdminArabicMiddleware:
    """Activate Arabic for admin requests without affecting the public API."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path_info.startswith("/admin/"):
            return self.get_response(request)
        with override("ar"):
            request.LANGUAGE_CODE = "ar"
            response = self.get_response(request)
            response.headers.setdefault("Content-Language", "ar")
            return response


class ArabicAdminSite(AdminSite):
    site_header = "لوحة إدارة دليل تطبيقات الحج والعمرة"
    site_title = "إدارة دليل الحج والعمرة"
    index_title = "لوحة التحكم"

    def get_app_list(self, request, app_label=None):
        app_list = super().get_app_list(request, app_label)
        for app in app_list:
            label = app["app_label"]
            app["name"] = SECTIONS.get(label, app["name"])
            for model in app["models"]:
                names = MODELS.get((label, model["object_name"].lower()))
                if names:
                    model["name"] = names[1]
        return app_list


class ArabicAdminConfig(AdminConfig):
    default_site = "config.admin_locale.ArabicAdminSite"


class ArabicChangeList(ChangeList):
    def __init__(self, request, model, *args, **kwargs):
        super().__init__(request, model, *args, **kwargs)
        names = MODELS.get((self.opts.app_label, self.opts.model_name))
        if names:
            self.title = names[1]


class ArabicAdminLabels:
    """Localize domain-specific form labels without altering model metadata."""

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if field is None:
            return field

        field.label = FIELDS.get(db_field.name, field.label)
        if db_field.choices:
            field.choices = [
                (value, CHOICES.get(value, label))
                for value, label in field.choices
            ]
        return field

    def get_fieldsets(self, request, obj=None):
        return [
            (HEADINGS.get(name, name), options)
            for name, options in super().get_fieldsets(request, obj)
        ]

    def get_changelist(self, request, **kwargs):
        return ArabicChangeList

    def render_change_form(self, request, context, add=False, change=False,
                           form_url="", obj=None):
        names = MODELS.get((self.opts.app_label, self.opts.model_name))
        if names:
            action = "إضافة" if add else "تعديل" if context["has_change_permission"] else "عرض"
            context["title"] = f"{action} {names[0]}"
        return super().render_change_form(request, context, add, change, form_url, obj)
