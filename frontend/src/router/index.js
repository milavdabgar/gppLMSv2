import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import GeneralList from "@/components/GeneralList.vue";
import GeneralEdit from "@/components/GeneralEdit.vue";
import UserLogin from '@/components/UserLogin.vue';
import UserRegistration from '@/components/UserRegistration.vue';
import BrowseBooks from '@/components/BrowseBooks.vue';
import BrowseGenres from '@/components/BrowseGenres.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },

  {
    path: '/login',
    name: 'UserLogin',
    component: UserLogin
  },
  {
    path: '/register',
    name: 'UserRegister',
    component: UserRegistration
  },

  {
    path: '/browse-books',
    name: 'BrowseBooks',
    component: BrowseBooks
  },
  {
    path: '/browse-genres',
    name: 'BrowseGenres',
    component: BrowseGenres
  },

  {
    path: "/books/edit/:id",
    name: "EditBook",
    component: GeneralEdit,
    props: (route) => ({ type: "Book", id: route.params.id }),
  },

  {
    path: "/genres/edit/:id",
    name: "EditGenre",
    component: GeneralEdit,
    props: (route) => ({ type: "Genre", id: route.params.id }),
  },

  {
    path: "/authors/edit/:id",
    name: "EditAuthor",
    component: GeneralEdit,
    props: (route) => ({ type: "Author", id: route.params.id }),
  },

  {
    path: "/books",
    component: GeneralList,
    props: {
      resourceType: "books",
      editRoute: "EditBook",
    },
  },

  {
    path: "/authors",
    component: GeneralList,
    props: {
      resourceType: "authors",
      editRoute: "EditAuthor",
    },
  },

  {
    path: "/genres",
    component: GeneralList,
    props: {
      resourceType: "genres",
      editRoute: "EditGenre",
    },
  },
];

const router = new VueRouter({
  routes,
});

export default router;
