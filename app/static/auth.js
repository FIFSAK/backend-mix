new Vue({
    el: '#auth',
    data: {
        token: '',
        refresh_token: '',


    },
    methods: {
        register: function (name, password) {
            const vm = this;
            axios.post('api/register/', {body: {name: name, password: password}})
                .then(function (response) {
                    console.log('API Response:', response);
                    if (response.username !== "A user with that username already exists.") {
                        axios.post('api/token/', {body: {username: name, password: password}})
                            .then(function (response) {
                                console.log('API Response:', response);
                                vm.token = response.access;
                                vm.refresh_token = response.refresh;
                            })
                            .catch(function (error) {
                                console.log(error);
                            });
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        login: function (name, password) {
            axios.post('api/token/', {body: {username: name, password: password}})
                .then(function (response) {
                    console.log('API Response:', response);
                    vm.token = response.access;
                    vm.refresh_token = response.refresh;
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    },

});

