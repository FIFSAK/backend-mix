new Vue({
    el: '#cart',
    data: {
        cartItem: '',
    },
    methods: {
        fetchData: function () {
            const params = new URLSearchParams(window.location.search);
            let cartId = params.get('id') || '';
            let query = '/api/clothes/?id=' + cartId;

            axios.get(query)
                .then((response) => { // Use arrow function here
                    console.log('API Response:', response);

                    this.cartItem = response.data.results[0];
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
