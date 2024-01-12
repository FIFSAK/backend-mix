new Vue({
    el: '#clothes-cards',
    data: {
        clothes: [],
        sortType: '',
        selectedFilter: [],
        searchQuery: '',
        cartItem: '',
    },
    methods: {
        searchForm: function () {
            console.log(this.searchQuery); // Now this will log the input from the search box
            this.fetchData();
        },
        orderType: function (sortValue) {
            console.log('Order type changed to:', sortValue);
            this.sortType = sortValue;
            this.fetchData();
        },
        updateFilter: function (filter) {
            let index = this.selectedFilter.indexOf(filter);

            if (index > -1) {
                this.selectedFilter.splice(index, 1);
            } else {
                this.selectedFilter.push(filter);
            }
            this.fetchData();
        },

        fetchData: function () {
            const params = new URLSearchParams(window.location.search);
            let category = params.get('category') || '';
            let query = '/api/clothes/?category=' + category;

            if (this.sortType) {
                query += "&ordering=" + this.sortType;
            }
            if (this.selectedFilter.length) {
                query += "&search=" + this.selectedFilter.join('&');
            }

            if (this.searchQuery) {
                query += "&search=" + this.searchQuery;
            }

            const vm = this;

            axios.get(query)
                .then(function (response) {
                    // console.log('API Response:', response);

                    vm.clothes = response.data.results;
                    // for (i = 0; i < vm.clothes.length; i++) {
                    //     console.log(vm.clothes[i].id)
                    // }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    },
    created: function () {
        this.fetchData();
    },
});
