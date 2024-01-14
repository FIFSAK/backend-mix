var app = new Vue({
    el: '#clothes-cards',
    data: {
        clothes: [],
        sortType: '',
        selectedFilter: [],
        searchQuery: '',
        cartItem: '',
        lower_bound_price: '',
        upper_bound_price: '',
        page_count: '',
        currentPage: 1,
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
        priceFilter: function (lower_bound_price, upper_bound_price) {
            this.lower_bound_price = lower_bound_price;
            this.upper_bound_price = upper_bound_price
            this.fetchData();
        },
        changePage(direction) {
            if (direction === 'next' && this.currentPage < this.page_count) {
                this.currentPage++;
            } else if (direction === 'prev' && this.currentPage > 1) {
                this.currentPage--;
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
            if (this.upper_bound_price && this.lower_bound_price) {
                query += "&lprice=" + this.lower_bound_price + "&uprice=" + this.upper_bound_price;
            }
            query += `&page=${this.currentPage}`;
            console.log(query)
            const vm = this;
            axios.get(query)
                .then(function (response) {
                    console.log('API Response:', response);

                    vm.clothes = response.data.results;
                    vm.page_count = Math.ceil(response.data.count/6);
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

window.vueApp = app;
