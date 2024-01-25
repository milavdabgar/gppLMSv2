import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import MyLoansView from "@/views/MyLoansView.vue"
import LibrarianDashboardView from "@/views/LibrarianDashboardView.vue";
import LibrarianDashboard from "@/components/LibrarianDashboard.vue";
import MemberDashboard from "@/components/MemberDashboard.vue";
import GeneralList from "@/components/GeneralList.vue";
import GeneralEdit from "@/components/GeneralEdit.vue";
import UserRegistration from '@/components/UserRegistration.vue';
import UserLogin from '@/components/UserLogin.vue';
import UserLogout from '../components/UserLogout.vue';
import ForgotPassword from '@/components/ForgotPassword.vue';
import ChangePassword from '@/components/ChangePassword.vue';
import SelectRole from '@/components/SelectRole.vue';
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
    path: "/member/loans",
    name: "MyLoansView",
    component: MyLoansView,
  },
  {
    path: "/librarian/dashboard",
    name: "LibrarianDashboardView",
    component: LibrarianDashboardView,
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
    path: '/logout',
    name: 'Logout',
    component: UserLogout
  },
  {
    path: '/register',
    name: 'UserRegister',
    component: UserRegistration
  },
  {
    path: '/reset',
    name: 'ForgotPassword',
    component: ForgotPassword
  },
  {
    path: '/change',
    name: 'ChangePassword',
    component: ChangePassword
  },
  {
    path: '/select_role',
    name: 'SelectRole',
    component: SelectRole
  },

  {
    path: '/librarian/home',
    name: 'LibrarianDashboard',
    component: LibrarianDashboard
  },

  {
    path: '/member/home',
    name: 'MemberDashboard',
    component: MemberDashboard
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
    path: "/users/edit/:id",
    name: "EditUser",
    component: GeneralEdit,
    props: (route) => ({ type: "User", id: route.params.id }),
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

  {
    path: "/users",
    component: GeneralList,
    props: {
      resourceType: "users",
      editRoute: "EditUser",
    },
  },
];

const router = new VueRouter({
  routes,
});

export default router;
