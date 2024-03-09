import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/HomeView.vue";
import MyLoansView from "@/views/MyLoansView.vue";
import LibrarianDashboardView from "@/views/LibrarianDashboardView.vue";
import MemberDashboardView from "@/views/MemberDashboardView.vue";

import UserRegistration from "@/components/auth/UserRegistration.vue";
import UserLogin from "@/components/auth/UserLogin.vue";
import UserLogout from "../components/auth/UserLogout.vue";
import ForgotPassword from "@/components/auth/ForgotPassword.vue";
import ChangePassword from "@/components/auth/ChangePassword.vue";

import RoleSelectionComponent from "@/components/RoleSelectionComponent.vue";
import BookLoanDetailsComponent from "@/components/BookLoanDetailsComponent.vue";

import BrowseBooks from "@/components/BrowseBooks.vue";
import BrowseGenres from "@/components/BrowseGenres.vue";
import GeneralList from "@/components/GeneralList.vue";
import GeneralEdit from "@/components/GeneralEdit.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/select-role",
    name: "SelectRole",
    component: RoleSelectionComponent,
  },

  {
    path: "/member/loans",
    name: "MyLoansView",
    component: MyLoansView,
  },

  {
    path: "/librarian/home",
    name: "LibrarianDashboardView",
    component: LibrarianDashboardView,
  },

  {
    path: "/member/home",
    name: "MemberDashboardView",
    component: MemberDashboardView,
  },
  {
    path: "/loan-details/:id",
    name: "LoanDetails",
    component: BookLoanDetailsComponent,
  },

  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },

  {
    path: "/login",
    name: "UserLogin",
    component: UserLogin,
  },
  {
    path: "/logout",
    name: "Logout",
    component: UserLogout,
  },
  {
    path: "/register",
    name: "UserRegister",
    component: UserRegistration,
  },
  {
    path: "/reset",
    name: "ForgotPassword",
    component: ForgotPassword,
  },
  {
    path: "/change",
    name: "ChangePassword",
    component: ChangePassword,
  },
  {
    path: "/browse-books",
    name: "BrowseBooks",
    component: BrowseBooks,
  },
  {
    path: "/browse-genres",
    name: "BrowseGenres",
    component: BrowseGenres,
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
