import router from "@/router";
export default function () {
  router.addRoute({
    name: "lotzappAdmin",
    path: "/mila_lotzapp/admin",
    component: () =>
      import("@/extensions/mila_lotzapp/components/LotzappAdmin.vue"),
  });
}
