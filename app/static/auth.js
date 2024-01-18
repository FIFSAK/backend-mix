new Vue({
    el: '#auth',
    data: {
        username: '',
        password: '',
        token: '',
        refresh_token: '',
    },
    methods: {
        register() {
            const vm = this;
            axios.post('api/register/', {username: vm.username, password: vm.password})
                .then(response => {
                    console.log('API Response:', response);
                    // Successful registration
                    if (response.data.username !== "A user with that username already exists.") {
                        console.log("User successfully registered.");
                        // Optionally, automatically log the user in after registration
                        vm.login();
                    } else {
                        // Handle the case where the username already exists
                        console.log("A user with that username already exists. Please choose a different username.");
                        // You can set a flag or message to inform the user that the username is taken
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        },
        login() {
            const vm = this;
            axios.post('api/token/', {username: vm.username, password: vm.password})
                .then(response => {
                    console.log('API Response:', response);
                    vm.token = response.data.access;
                    vm.refresh_token = response.data.refresh;
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
});
