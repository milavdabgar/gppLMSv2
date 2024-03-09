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
import { userService, authorService, genreService, bookService } from "@/services/ApiService";

const serviceMap = {
    users: userService,
    authors: authorService,
    genres: genreService,
    books: bookService,
};

export default {
    props: {
        resourceType: {
            type: String,
            required: true,
        },
        editRoute: {
            type: String,
            required: true,
        },
    },

    data() {
        return {
            items: [],
            title: "",
        };
    },

    created() {
        this.fetchData();
    },

    watch: {
        "$route.params": {
            handler() {
                this.fetchData();
            },
            immediate: true,
        },
    },

    methods: {
        async fetchData() {
            try {
                const service = serviceMap[this.resourceType];
                const data = await service.getAll();
                this.items = data.map((item) => ({
                    id: item.id,
                    displayText: item.title || item.name || item.email,
                }));
                this.title = this.resourceType.charAt(0).toUpperCase() + this.resourceType.slice(1);
            } catch (error) {
                console.error(error);
            }
        },
    },
};
</script>