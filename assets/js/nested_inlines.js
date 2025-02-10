(function($) {
    $(document).ready(function() {
        // Функция для инициализации вложенных инлайнов
        function initializeNestedInlines() {
            $('.inline-group').each(function() {
                var group = $(this);
                group.find('.inline-related').each(function() {
                    var item = $(this);
                    var nestedInlines = item.find('.inline-group');
                    if (nestedInlines.length) {
                        // Перемещаем вложенные инлайны внутрь родительского элемента
                        nestedInlines.each(function() {
                            var nested = $(this);
                            nested.detach().appendTo(item.find('fieldset:first'));
                        });
                    }
                });
            });
        }

        // Инициализация при загрузке страницы
        initializeNestedInlines();

        // Обработка добавления новых форм
        $(document).on('formset:added', function(event, $row, formsetName) {
            initializeNestedInlines();
        });
    });
})(django.jQuery);