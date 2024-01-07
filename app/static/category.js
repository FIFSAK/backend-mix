new Vue({
    el: '#category',
    data: {
        clothes: []
    },
    methods: {
        loadCategory: function (category_type) {
            const vm = this;
            axios.get('/api/clothes/?search=' + category_type)
                .then(function (response) {
                    vm.clothes = response.data.results;
                    console.log(response.data.results);
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    },

});
