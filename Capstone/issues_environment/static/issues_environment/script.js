
const App = {
    delimiters: ['[[', ']]'],
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
    mounted () { // mopunted hook runs when html is loaded
        this.csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
        console.log(this.csrfmiddlewaretoken)
    },
    methods: {
        getInfo() {
            // need to use searchEntry to get data from table? 
            //save first then GET?
            // this.itemsToDo.push(this.searchEntry)
            // print('')}
            axios({
                method: 'post',
                url: '/country_issue_info',
                data: { message: 'hello', term: 'united' },
                headers: {
                    'X-CSRFToken': this.csrfmiddlewaretoken
                }
            })
                .then(res => {
                    console.log(res.data)
                })
        }

    },
}

Vue.createApp(App).mount('#app')
