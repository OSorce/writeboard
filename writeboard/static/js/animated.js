;(function($) {
    $.fn.animated = function(options) {
        var opts = $.extend({}, jQuery.fn.animated.defaults, options);
        
        self = $(this);
        
        self.each(function(i, e) {
            var cls = $(e).data('animated');
            if (cls.match('In') != null) {
                $(e).css('visibility', 'hidden');
            }
        });
        
        var animate_getter = opts.animate_getter;
        
        self.waypoint( function() {
            var e = $(this).attr('element');
            var cls = animate_getter($(e));
            
            if (cls.match('In') != null) {
                $(e).css('visibility', 'visible');
            }
            
            $(e).addClass(cls).addClass('animated');
        }, {
            offset: '75%'
        });
    };
    
    $.fn.animated.defaults = {
        'animate_getter': function(e) { return e.data('animated'); },
    };
})(jQuery);