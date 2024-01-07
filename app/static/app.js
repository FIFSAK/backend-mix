new Vue({
    el: '#clothes-cards',
    data: {
        clothes: []
    },
    created: function () {
        const params = new URLSearchParams(window.location.search);
        let category = params.get('category');
        console.log(category);

        const vm = this;
        axios.get('/api/clothes/?category=' + category)
            .then(function (response) {
                vm.clothes = response.data.results; // Assign data to clothes
                console.log(response.data.results); // Log to ensure data is received
            })
            .catch(function (error) {
                console.log(error); // Log any error
            });
    },
});