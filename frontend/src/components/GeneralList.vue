<template>
    <div>
        <ul>
            <h1>{{ title }}</h1>
            <li v-for="item in items" :key="item.id">
                <router-link :to="{ name: editRoute, params: { id: item.id } }">
                    {{ item.displayText }}
                </router-link>
            </li>
        </ul>
    </div>
</template>
  
<script>
import axios from 'axios'

export default {
    props: {
        resourceType: {
            type: String,
            required: true
        },
        editRoute: {
            type: String,
            required: true
        }
    },

    data() {
        return {
            items: [],
            title: ''
        }
    },

    created() {
        this.fetchData()
    },

    // GeneralList.vue

    watch: {
        '$route.params': {
            handler() {
                this.fetchData()
            },
            immediate: true // fetch on initial load
        }
    },

    methods: {
        fetchData() {
            if (this.resourceType === 'books') {
                this.fetchBooks()
            } else if (this.resourceType === 'authors') {
                this.fetchAuthors()
            } else if (this.resourceType === 'genres') {
                this.fetchGenres()
            } else if (this.resourceType === 'users') {
                this.fetchUsers()
            }
        },

        fetchBooks() {
            axios.get('http://localhost:5000/api/books')
                .then(res => {
                    let books = res.data.map(book => {
                        return {
                            id: book.id,
                            displayText: book.title
                        }
                    })

                    this.items = books
                    this.title = 'Books'
                })
        },

        fetchAuthors() {
            axios.get('http://localhost:5000/api/authors')
                .then(res => {
                    let authors = res.data.map(author => {
                        return {
                            id: author.id,
                            displayText: author.name
                        }
                    })

                    this.items = authors
                    this.title = 'Authors'
                })
        },

        fetchGenres() {
            axios.get('http://localhost:5000/api/genres')
                .then(res => {
                    let genres = res.data.map(genre => {
                        return {
                            id: genre.id,
                            displayText: genre.name
                        }
                    })

                    this.items = genres
                    this.title = 'Genres'
                })
        },

        fetchUsers() {
            axios.get('http://localhost:5000/api/users')
                .then(res => {
                    let users = res.data.map(user => {
                        return {
                            id: user.id,
                            displayText: user.email
                        }
                    })

                    this.items = users
                    this.title = 'Users'
                })
        }
    }
}
</script>