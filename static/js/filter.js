$(document).ready(function () {
    // Filter Start
    $(".checkbox").on('click', function () {
        var _filterObj = {};
        $(".checkbox").each(function (index, ele) {
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
                return el.value;
            });
        });

        // Run Ajax
        $.ajax({
        	url:'/filter',
        	data:_filterObj,
        	dataType:'json',
        	beforeSend:function(){
        		$(".result").empty();
        		$(".result").append(`<h2 class='font-semibold text-center text-2xl'>Loading......</h2>`);
        	},
        	success:function(res){
        		// console.log(res.data);
        		$(".result").empty();
                for (let i = 0; i<res.data.length; i++){
                    let temp = res.data[i];
                    let html = `<div class="border rounded-md flex items-center justify-between p-6">
                                        <b>${temp.search_keyword}</b>
                                        <b>Total Result: ${temp.search_results}</b>
                                        <b>${temp.search_date}</b>
                                    </div>`
                    $(".result").append(html);

                }
        	}
        });
    });
});