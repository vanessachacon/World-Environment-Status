
const App = {
    delimiters: ['[[', ']]'],
    el: '#app',
    data() {
        return {
            message: 'Testing!!!',
            searchEntry: '',
            searchResult: '',
            countryIssueInfo: [],
            csrfmiddlewaretoken: ''

        }
    },
    created() { // created hook runs when vue app is created
        // this.getInfo()
    },
    mounted () { // mounted hook runs when html is loaded
        this.csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
        console.log(this.csrfmiddlewaretoken)
    },
    methods: {
        getInfo() {

            axios({
                method: 'post',
                url: '/country_issue_info',
                data: { this.searchEntry },
                headers: {
                    'X-CSRFToken': this.csrfmiddlewaretoken
                }
            })
                .then(res => {
                    console.log(res.data)
                    searchResult.push(res.data)
                    console.log(searchResult)
                })
        }

    },
}

Vue.createApp(App).mount('#app')



            // need to use searchEntry to get data from table? 
            //save first then GET?
            // this.itemsToDo.push(this.searchEntry)
            // print('')}