from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class MarketingDepartment(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: BoldBrends International'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: Мы поможем вам найти бренды, которые вам нужны'))
    
    class Meta:
        verbose_name = _('Отдел маркетинга')
        verbose_name_plural = _('Отделы маркетинга')

    def __str__(self):
        return self.title


class MarketingDepartmentChapters(models.Model):
    marketing_department = models.ForeignKey(MarketingDepartment, verbose_name=_('Отдел маркетинга'), on_delete=models.CASCADE, related_name='chapters')
    number = models.CharField(verbose_name=_('Номер главы'), max_length=255, help_text=_('Например: 01'))
    title = models.CharField(verbose_name=_('Название главы'), max_length=255, help_text=_('Например: Глава 1'))

    class Meta:
        verbose_name = _('Глава отдела маркетинга')
        verbose_name_plural = _('Главы отделов маркетинга')
        ordering = ['-id']

    def __str__(self):
        return f'{self.title} - {self.number}'


class CompanyAchievements(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: BoldBrends International'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: совместно создаем прочную ...'))

    class Meta:
        verbose_name = _('Достижение компании')
        verbose_name_plural = _('Достижения компании')

    def __str__(self):
        return f'{self.title} - {self.sub_title}'


class CompanyAchievementsItems(models.Model):
    company_achievement = models.ForeignKey(CompanyAchievements, verbose_name=_('Достижение компании'), on_delete=models.CASCADE, related_name='items')
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Топ-1'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: маркетинговая компания по версии The Great 2023...'))

    class Meta:
        verbose_name = _('Достижение компании')
        verbose_name_plural = _('Достижения компании')
        ordering = ['-id']

    def __str__(self):
        return f'{self.title} - {self.sub_title}'


class CompanyChallenges(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Что мешает вашему бизнесу?'))

    class Meta:
        verbose_name = _('Проблема компании')
        verbose_name_plural = _('Проблемы компании')

    def __str__(self):
        return self.title


class CompanyChallengesItems(models.Model):
    company_challenge = models.ForeignKey(CompanyChallenges, verbose_name=_('Проблема компании'), on_delete=models.CASCADE, related_name='items')
    logo = models.FileField(verbose_name=_('Логотип'), upload_to='company_challenges_logos/')
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Отсутствие маркетинговой стратегии'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: Без четкого плана результаты будут хаотичными.'))

    class Meta:
        verbose_name = _('Проблема компании')
        verbose_name_plural = _('Проблемы компании')
        ordering = ['-id']

    def __str__(self):
        return self.title


class CompanyServices(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Выводим компании в ТОП ...'))

    class Meta:
        verbose_name = _('Услуга компании')
        verbose_name_plural = _('Услуги компании')
    
    def __str__(self):
        return self.title
    

class Tags(models.Model):
    tags = models.CharField(verbose_name=_('Теги'), max_length=255, help_text=_('Например: Маркетинговая стратегия, SEO, SMM, PR'))

    class Meta:
        verbose_name = _('Тег услуги компании')
        verbose_name_plural = _('Теги услуг компании')
        ordering = ['-id']

    def __str__(self):
        return self.tags


class SocialMedia(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Instagram'))
    logo = models.FileField(verbose_name=_('Логотип'), upload_to='social_media_logos/')
    subscribers = models.CharField(verbose_name=_('Подписчики'), max_length=255, help_text=_('Например: +10,5 подписчиков'))

    class Meta:
        verbose_name = _('Социальная сеть')
        verbose_name_plural = _('Социальные сети')

    def __str__(self):
        return self.title


class CompanyServicesItems(models.Model):
    company_service = models.ForeignKey(CompanyServices, verbose_name=_('Услуга компании'), on_delete=models.CASCADE, related_name='items')
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Маркетинговая стратегия'))
    image = models.FileField(verbose_name=_('Изображение'), upload_to='company_services_images/')
    tags = models.ManyToManyField(Tags, verbose_name=_('Теги'), related_name='items')
    link = models.URLField(verbose_name=_("Ссылка для переноса"), null=True, blank=True)


    class Meta:
        verbose_name = _('Услуга компании')
        verbose_name_plural = _('Услуги компании')
        ordering = ['-id']

    def __str__(self):
        return self.title


class CompanyPosts(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Как мы помогли другим...'))

    class Meta:
        verbose_name = _('Пост компании')
        verbose_name_plural = _('Посты компании')

    def __str__(self):
        return self.title


class CompanyPostsItems(models.Model):
    company_post = models.ForeignKey(CompanyPosts, verbose_name=_('Пост компании'), on_delete=models.CASCADE, related_name='items')
    image = models.FileField(verbose_name=_('Изображение'), upload_to='company_posts_images/')
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Увеличили выручку корейского ресторана на 70%...'))
    company_name = models.CharField(verbose_name=_('Название компании'), max_length=255, help_text=_('Например: Корейский ресторан'))
    created_at = models.DateField(verbose_name=_('Дата создания'), auto_now_add=True)
    tags = models.ManyToManyField(Tags, verbose_name=_('Теги'), related_name='post_items')
    social_media = models.ManyToManyField(SocialMedia, verbose_name=_('Социальные сети'), related_name='post_items')

    class Meta:
        verbose_name = _('Пост компании')
        verbose_name_plural = _('Посты компании')
        ordering = ['-id']

    def __str__(self):
        return self.title


class CompanyPostsItemsTasks(models.Model):
    company_post_item = models.ForeignKey(CompanyPostsItems, verbose_name=_('Пост компании'), on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(verbose_name=_('Название задачи'), max_length=255, help_text=_('Например: Задача клиента'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Описание задачи'), help_text=_('Например: Основной задачей клиента было увеличить выручку корейского ресторана на 70%'), blank=True, null=True)

    class Meta:
        verbose_name = _('Задача поста компании')
        verbose_name_plural = _('Задачи постов компании')
        ordering = ['-id']

    def __str__(self):
        return self.title


class CompanyPostsItemsTarget(models.Model):
    company_post_item = models.ForeignKey(CompanyPostsItems, verbose_name=_('Пост компании'), on_delete=models.CASCADE, related_name='target')
    title = models.CharField(verbose_name=_('Название рекламы'), max_length=255, help_text=_('Например: реклама клиента'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Описание рекламы'), help_text=_('Например: Основной реклама клиента было увеличить выручку корейского ресторана на 70%'), blank=True, null=True)

    class Meta:
        verbose_name = _('Реклама поста компании')
        verbose_name_plural = _('Реклама постов компании')
        ordering = ['-id']

    def __str__(self):
        return self.title


class CompanyPostsItemsImages(models.Model):
    company_post_item = models.ForeignKey(CompanyPostsItems, verbose_name=_('Пост компании'), on_delete=models.CASCADE, related_name='images')
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Фотография 1'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: Фотография 1'))

    class Meta:
        verbose_name = _('Изображение поста компании')
        verbose_name_plural = _('Изображения постов компании')
        ordering = ['-id']

    def __str__(self):
        return self.title


class CompanyPostsItemsResult(models.Model):
    company_post_item = models.ForeignKey(CompanyPostsItems, verbose_name=_('Пост компании'), on_delete=models.CASCADE, related_name='results')
    header = models.CharField(verbose_name=_('Заголовок'), max_length=255, help_text=_('Например: Результаты'))
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Результаты'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: Мы помогли увеличить выручку корейского ресторана на 70%'))

    class Meta:
        verbose_name = _('Результат поста компании')
        verbose_name_plural = _('Результаты постов компании')
        ordering = ['-id']

    def __str__(self):
        return self.title


class CompanyPartners(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Наши партнеры'))

    class Meta:
        verbose_name = _('Партнер компании')
        verbose_name_plural = _('Партнеры компании')

    def __str__(self):
        return self.title


class CompanyPartnersItems(models.Model):
    company_partner = models.ForeignKey(CompanyPartners, verbose_name=_('Партнер компании'), on_delete=models.CASCADE, related_name='items')
    company_name = models.CharField(verbose_name=_('Название компании'), max_length=255, help_text=_('Например: Bigser'))
    company_logo = models.FileField(verbose_name=_('Логотип компании'), upload_to='company_partners_logos/')

    class Meta:
        verbose_name = _('Партнер компании')
        verbose_name_plural = _('Партнеры компании')
        ordering = ['-id']

    def __str__(self):
        return self.company_logo.name


class PartnersReviews(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Отзывы наших партнеров'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: Мы очень довольны работой с компанией BoldBrends...'))

    class Meta:
        verbose_name = _('Отзыв партнера')
        verbose_name_plural = _('Отзывы партнеров')

    def __str__(self):
        return self.title


class PartnersReviewsItems(models.Model):
    rate = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    partner_review = models.ForeignKey(PartnersReviews, verbose_name=_('Отзыв партнера'), on_delete=models.CASCADE, related_name='items')
    rating = models.IntegerField(verbose_name=_('Рейтинг'), choices=rate)
    user_image = models.FileField(verbose_name=_('Изображение пользователя'), upload_to='partners_reviews_images/')
    user_name = models.CharField(verbose_name=_('Имя пользователя'), max_length=255, help_text=_('Например: John Doe'))
    user_position = models.CharField(verbose_name=_('Должность пользователя'), max_length=255, help_text=_('Например: CEO'))
    text = models.TextField(verbose_name=_('Текст отзыва'), help_text=_('Например: Мы очень довольны работой с компанией BoldBrends...'))

    class Meta:
        verbose_name = _('Отзыв партнера')
        verbose_name_plural = _('Отзывы партнеров')
        ordering = ['-id']

    def __str__(self):
        return self.user_name


class CompanyApplication(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Оставить заявку на партнерство'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: Мы свяжемся с вами в ближайшее время'))

    class Meta:
        verbose_name = _('Заявка на партнерство')
        verbose_name_plural = _('Заявки на партнерство')

    def __str__(self):
        return self.title


class BusinessType(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Ресторан'))

    class Meta:
        verbose_name = _('Тип бизнеса')
        verbose_name_plural = _('Типы бизнеса')
        ordering = ['name']

    def __str__(self):
        return self.name


class PromotionType(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: SMM продвижение'))

    class Meta:
        verbose_name = _('Тип продвижения')
        verbose_name_plural = _('Типы продвижения')
        ordering = ['name']

    def __str__(self):
        return self.name


class SocialType(models.Model):
    name = models.CharField(verbose_name=_("Название"), max_length=255, help_text=_("Например: Instagram"))

    class Meta:
        verbose_name = _("Тип соц. сетей")
        verbose_name_plural = _("Типы соц. сетей")
    
    def __str__(self):
        return self.name
    

class SiteStatusType(models.Model):
    name = models.CharField(verbose_name=_("Название"), max_length=255, help_text=_('Новый сайт'))

    class Meta:
        verbose_name = _("Статус Сайта")
        verbose_name_plural = _("Статус Сайт")
        ordering = ['name']

    def __str__(self):
        return self.name


class SiteType(models.Model):
    name = models.CharField(verbose_name=_("Название"), max_length=255, help_text=_('Лендинг'))

    class Meta:
        verbose_name = _("Тип сайта")
        verbose_name_plural = _("Типы сайта")
        ordering = ['name']

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    name = models.CharField(verbose_name=_("Название"), max_length=255, help_text=_('Нейминг'))

    class Meta:
        verbose_name = _("Услуги продвижения")
        verbose_name_plural = _("Услуги продвижения")
        ordering = ['name']

    def __str__(self):
        return self.name


class VideoType(models.Model):
    name = models.CharField(verbose_name=_("Название"), max_length=255, help_text=_('Фотосессия'))

    class Meta:
        verbose_name = _("Тип видео")
        verbose_name_plural = _("Типы видео")
        ordering = ['name']

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(verbose_name=_("Название"), max_length=255, help_text=_('Аналитика'))

    class Meta:
        verbose_name = _("Задача")
        verbose_name_plural = _("Задачи")
        ordering = ['name']

    def __str__(self):
        return self.name


class ApplicationForm(models.Model):
    sender_name = models.CharField(verbose_name=_('Имя отправителя'), max_length=255, help_text=_('Например: John Doe'))
    sender_phone = models.CharField(verbose_name=_('Телефон отправителя'), max_length=255, help_text=_('Например: +7 999 999 99 99'))
    sender_email = models.EmailField(verbose_name=_('Email отправителя'), max_length=255, help_text=_('Например: john.doe@example.com'))
    business_type = models.ManyToManyField(BusinessType, verbose_name=_('Типы бизнеса'))
    promotion_type = models.ManyToManyField(PromotionType, verbose_name=_('Типы продвижения'))
    social_type = models.ManyToManyField(SocialType, verbose_name=_('Типы соц. сетей'))
    quantity_of_publications = models.TextField(null=True, blank=True, verbose_name=_('Количество публикаций в месяц'))
    site_status = models.ManyToManyField(SiteStatusType, verbose_name=_("Статус сайта"))
    purpose_of_promotion = models.CharField(max_length=255, verbose_name=_("Цель продвижения"), null=True, blank=True)
    site_type = models.ManyToManyField(SiteType, verbose_name=_("Типы сайта"))
    service_type = models.ManyToManyField(ServiceType, verbose_name=_("Услуги"))
    video_type = models.ManyToManyField(VideoType, verbose_name=_("Типы видео"))
    task_type = models.ManyToManyField(TaskType, verbose_name=_("Типы Задач"))

    class Meta:
        verbose_name = _('Форма заявки на партнерство')
        verbose_name_plural = _('Формы заявок на партнерство')

    def __str__(self):
        return self.sender_name


class StaticPages(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: О компании'))
    content = models.TextField(verbose_name=_('Контент'), help_text=_('Например: Мы компания BoldBrends...'))
    image = models.FileField(verbose_name=_('Изображение'), upload_to='static_pages_images/')
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = _('Статическая страница')
        verbose_name_plural = _('Статические страницы')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while StaticPages.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CompanyTeam(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Команда, которой можно доверять'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: Мы команда, которая поможет вам...'))

    class Meta:
        verbose_name = _('Команда компании')
        verbose_name_plural = _('Команды компании')

    def __str__(self):
        return self.title


class CompanyTeamItems(models.Model):
    company_team = models.ForeignKey(CompanyTeam, verbose_name=_('Команда компании'), on_delete=models.CASCADE, related_name='items')
    name = models.CharField(verbose_name=_('Имя'), max_length=255, help_text=_('Например: Мамбетова Алия'))
    position = models.CharField(verbose_name=_('Должность'), max_length=255, help_text=_('Например: Руководитель отдела мобилогрфии'))
    image = models.FileField(verbose_name=_('Изображение'), upload_to='company_team_images/')

    class Meta:
        verbose_name = _('Участник команды компании')
        verbose_name_plural = _('Участники команды компании')
        ordering = ['-id']

    def __str__(self):
        return self.name


class CompanyAdvertising(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Контент который продает'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: Мы создаем визуалы, которые выделяют ваш бренд среди конкурентов'))

    class Meta:
        verbose_name = _('Реклама компании')
        verbose_name_plural = _('Реклама компании')

    def __str__(self):
        return self.title


class CompanyAdvertisingItems(models.Model):
    company_advertising = models.ForeignKey(CompanyAdvertising, verbose_name=_('Реклама компании'), on_delete=models.CASCADE, related_name='items')
    image = models.FileField(verbose_name=_('Изображение'), upload_to='company_advertising_images/')

    class Meta:
        verbose_name = _('Реклама компании')
        verbose_name_plural = _('Реклама компании')
        ordering = ['-id']

    def __str__(self):
        return self.image.name


class CompanyVideoReviews(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Видеоотзывы от наших клиентов'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: Что говорят наши клиенты о нас'))

    class Meta:
        verbose_name = _('Видеоотзывы от наших клиентов')
        verbose_name_plural = _('Видеоотзывы от наших клиентов')

    def __str__(self):
        return self.title


class CompanyVideoReviewsItems(models.Model):
    company_video_review = models.ForeignKey(CompanyVideoReviews, verbose_name=_('Видеоотзывы от наших клиентов'), on_delete=models.CASCADE, related_name='items')
    video = models.URLField(verbose_name=_('Видео'), help_text=_("Ссылка видео с ютуба"))

    class Meta:
        verbose_name = _('Видеоотзывы от наших клиентов')
        verbose_name_plural = _('Видеоотзывы от наших клиентов')
        ordering = ['-id']

    def __str__(self):
        return self.company_video_review.title


class FAQ(models.Model):
    question = models.CharField(verbose_name=_('Вопрос'), max_length=255, help_text=_('Например: Как мы можем с вами связаться?'))
    answer = models.TextField(verbose_name=_('Ответ'), help_text=_('Например: Мы можем с вами связаться по телефону или email'))

    class Meta:
        verbose_name = _('Часто задаваемый вопрос')
        verbose_name_plural = _('Часто задаваемые вопросы')

    def __str__(self):
        return self.question


class CompanyBrending(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Брендинг - это не просто логотип и название'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: Почему Брендинг важен для вашего бизнеса?'))
    sub_title_2 = models.CharField(verbose_name=_('Подзаголовок 2'), max_length=255, help_text=_('Например: Это целостный образ вашей вашей компании, который формирует восприятие клиентов и выделяетвас на рынке'))

    class Meta:
        verbose_name = _('Брендинг компании')
        verbose_name_plural = _('Брендинг компании')

    def __str__(self):
        return self.title


class CompanyBrendingItems(models.Model):
    company_brending = models.ForeignKey(CompanyBrending, verbose_name=_('Брендинг компании'), on_delete=models.CASCADE, related_name='items')
    image = models.FileField(verbose_name=_('Изображение'), upload_to='company_brending_images/')

    class Meta:
        verbose_name = _('Брендинг компании')
        verbose_name_plural = _('Брендинг компании')
        ordering = ['-id']

    def __str__(self):
        return self.company_brending.title
    

class CompanyFeatures(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Создаем бренд, который говорит сам за себя'))

    class Meta:
        verbose_name = _('Преимущество компании')
        verbose_name_plural = _('Преимущества компании')

    def __str__(self):
        return self.title


class CompanyFeaturesItems(models.Model):
    company_feature = models.ForeignKey(CompanyFeatures, verbose_name=_('Преимущество компании'), on_delete=models.CASCADE, related_name='items')
    image = models.FileField(verbose_name=_('Изображение'), upload_to='company_features_images/')
    image_right = models.BooleanField(verbose_name=_('Изображение справа'), default=False)
    title = models.CharField(verbose_name=_("Название"), max_length=255, help_text=_("Например: Нейминг"))
    sub_title = models.CharField(verbose_name=_("Подзаголовок"), max_length=255, help_text=_("Например: Нейминг - это процесс создания уникального названия для вашего бизнеса"))
    description = models.TextField(verbose_name=_("Описание"), help_text=_("Например: Нейминг - это процесс создания уникального названия для вашего бизнеса"))
    tags = models.ManyToManyField(Tags, verbose_name=_("Теги"), related_name="features_items")

    class Meta:
        verbose_name = _('Преимущество компании')
        verbose_name_plural = _('Преимущества компании')
        ordering = ['-id']

    def __str__(self):
        return self.title


class VideoProduction(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Креатив, который выделяет ваш бренд'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: С более чем 10-летним опытом...'))

    class Meta:
        verbose_name = _('Видеопродукция')
        verbose_name_plural = _('Видеопродукция')

    def __str__(self):
        return self.title


class VideoProductionItems(models.Model):
    video_production = models.ForeignKey(VideoProduction, verbose_name=_('Видеопродукция'), on_delete=models.CASCADE, related_name='items')
    logo = models.FileField(verbose_name=_('Логотип'), upload_to='video_production_logos/')
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: В BoldBrends мы уверены'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: С более чем 10-летним опытом...'))
    video = models.URLField(verbose_name=_('Видео'), help_text=_("Ссылка на видео"))

    class Meta:
        verbose_name = _('Видеопродукция')
        verbose_name_plural = _('Видеопродукция')
        ordering = ['-id']

    def __str__(self):
        return self.video_production.title


class CRMService(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Наши услуги по интеграции CRM'))
    
    class Meta:
        verbose_name = _('Услуга CRM')
        verbose_name_plural = _('Услуги CRM')

    def __str__(self):
        return self.title


class CRMServiceItems(models.Model):
    crm_service = models.ForeignKey(CRMService, verbose_name=_('Услуга CRM'), on_delete=models.CASCADE, related_name='items')
    image = models.FileField(verbose_name=_('Изображение'), upload_to='crm_service_images/')
    image_right = models.BooleanField(verbose_name=_('Изображение справа'), default=False)
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Интеграция CRM'))
    tags = models.ManyToManyField(Tags, verbose_name=_("Теги"), related_name="crm_service_items")

    class Meta:
        verbose_name = _('Услуга CRM')
        verbose_name_plural = _('Услуги CRM')
        ordering = ['-id']

    def __str__(self):
        return self.title


class MarketingSupport(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Маркетинговая поддержка'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: Мы предлагаем маркетинговую поддержку...'))

    class Meta:
        verbose_name = _('Маркетинговая поддержка')
        verbose_name_plural = _('Маркетинговая поддержка')

    def __str__(self):
        return self.title


class MarketingSupportItems(models.Model):
    marketing_support = models.ForeignKey(MarketingSupport, verbose_name=_('Маркетинговая поддержка'), on_delete=models.CASCADE, related_name='items')
    logo = models.FileField(verbose_name=_('Логотип'), upload_to='video_production_logos/')
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: В BoldBrends мы уверены'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: С более чем 10-летним опытом...'))
    video = models.FileField(verbose_name=_('Видео'), upload_to='video_production_videos/')

    class Meta:
        verbose_name = _('Маркетинговая поддержка')
        verbose_name_plural = _('Маркетинговая поддержка')
        ordering = ['-id']

    def __str__(self):
        return self.marketing_support.title


class ServiceOffering(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Что мы делаем'))

    class Meta:
        verbose_name = _('Услуги которые мы предлагаем')
        verbose_name_plural = _('Услуги которые мы предлагаем')
    
    def __str__(self):
        return self.title


class ServiceOfferingItems(models.Model):
    service_offering = models.ForeignKey(ServiceOffering, verbose_name=_('Услуги которые мы предлагаем'), on_delete=models.CASCADE, related_name='items')
    image = models.FileField(verbose_name=_('Изображение'), upload_to='crm_service_images/')
    image_right = models.BooleanField(verbose_name=_('Изображение справа'), default=False)
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Интеграция CRM'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: Мы предлагаем интеграцию CRM...'))

    class Meta:
        verbose_name = _('Услуги которые мы предлагаем')
        verbose_name_plural = _('Услуги которые мы предлагаем')
        ordering = ['-id']

    def __str__(self):
        return self.title


class CompanyPostsItemsImagesGallery(models.Model):
    post_image = models.ForeignKey(CompanyPostsItemsImages, verbose_name=_('Изображение поста'), on_delete=models.CASCADE, related_name='gallery')
    image = models.FileField(verbose_name=_('Изображение'), upload_to='company_posts_images/')
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = _('Галерея изображений поста')
        verbose_name_plural = _('Галерея изображений постов')
        ordering = ['position']

    def __str__(self):
        return f"Изображение для {self.post_image.title}"


class BusinessCards(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Визитки'))

    class Meta:
        verbose_name = _('Визитка')
        verbose_name_plural = _('Визитки')

    def __str__(self):
        return f"Изображение для {self.title}"
    

class BusinessCardImages(models.Model):
    businesscards = models.ForeignKey(BusinessCards, verbose_name=_("Изображение визитки"), on_delete=models.CASCADE, related_name='businesscards')
    image = models.FileField(verbose_name=_('Изображение'), upload_to='business_card_images/')
    
    class Meta:
        verbose_name = _('Изображение визитки')
        verbose_name_plural = _('Изображения визитки')

    def __str__(self):
        return f"Изображение для {self.businesscards.title}"


class PrintingService(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Что мы печатаем?'))

    class Meta:
        verbose_name = _('Услуга печати логотипа')
        verbose_name_plural = _('Услуги печати логотипа')

    def __str__(self):
        return f"Лого для {self.title}"


class PrintLogo(models.Model):
    printing_service = models.ForeignKey(PrintingService, on_delete=models.CASCADE, related_name='items')
    logo = models.FileField(verbose_name=_('Логотип'), upload_to='print_logos/')

    class Meta:
        verbose_name = _('Логотип')
        verbose_name_plural = _('Логотипы')

    def __str__(self):
        return f"Лого для {self.printing_service.title}"


class DesignDevelopment(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Дизайн и Разработка'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: Мы создадим не просто мечты'))
    
    class Meta:
        verbose_name = _('Дизайн и разработка')
        verbose_name_plural = _('Дизайн и разработки')

    def __str__(self):
        return self.title


class DesignDevelopmentChapters(models.Model):
    design_development = models.ForeignKey(DesignDevelopment, verbose_name=_('Отдел маркетинга'), on_delete=models.CASCADE, related_name='chapters')
    number = models.CharField(verbose_name=_('Номер главы'), max_length=255, help_text=_('Например: 01'))
    title = models.CharField(verbose_name=_('Название главы'), max_length=255, help_text=_('Например: Глава 1'))

    class Meta:
        verbose_name = _('Глава дизайн и разработка')
        verbose_name_plural = _('Главы дизайн и разработки')
        ordering = ['-id']

    def __str__(self):
        return f'{self.title} - {self.number}'