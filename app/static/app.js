new Vue({
    el: '#clothes-cards',
    data: {
        clothes: [],
        sortType: '',
        selectedSizes: [],
        selectedBrand: [],
        searchQuery: '',
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
        updateSizes: function (size) {
            let index = this.selectedSizes.indexOf(size);

            if (index > -1) {
                this.selectedSizes.splice(index, 1);
            } else {
                this.selectedSizes.push(size);
            }
            this.fetchData();
        },
        updateBrand: function (brand) {
            let bindex = this.selectedBrand.indexOf(brand);

            if (bindex > -1) {
                this.selectedBrand.splice(bindex, 1);
            } else {
                this.selectedBrand.push(brand);
            }
            this.fetchData();
        },
        fetchData: function () {
            console.log('Fetching data with sort type:', this.sortType);
            const params = new URLSearchParams(window.location.search);
            let category = params.get('category') || ''; // Значение по умолчанию, если параметр отсутствует
            let query = '/api/clothes/?category=' + category;
            if (this.sortType) {
                query += "&ordering=" + this.sortType;
            }
            if (this.selectedSizes.length) {
                query += "&search=" + this.selectedSizes.join('&');
            }
            if (this.selectedBrand.length) {
                query += "&search=" + this.selectedBrand.join('&');
            }
            if(this.searchQuery){
                query += "&search=" + this.searchQuery;
            }
            const vm = this;
            console.log('Query URL:', query);

            axios.get(query)
                .then(function (response) {
                    console.log('API Response:', response);

                    vm.clothes = response.data.results;
                    for (i = 0; i < vm.clothes.length; i++) {
                        console.log(vm.clothes[i].id)
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    },
    created: function () {
        this.fetchData(); // Вызываем fetchData при создании
    },
});
