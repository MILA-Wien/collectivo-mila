<script setup lang="ts">
import ObjectTable from "@/components/datatable/ObjectTable.vue";
import { useMainStore } from "@/stores/main";
import { useMenuStore } from "@/stores/menu";
import TabPanel from "primevue/tabpanel";
import TabView from "primevue/tabview";
import { useI18n } from "vue-i18n";

const { t } = useI18n();
const mainStore = useMainStore();
const menuStore = useMenuStore();
menuStore.setTitle("Lotzapp");
</script>

<template>
  <div class="h-full tabview-full-height">
    <TabView lazy>
      <TabPanel :header="t('Synchronisation')">
        <ObjectTable
          :store="mainStore"
          :name="'lotzappSync'"
          :default-columns="['date', 'status', 'type', 'status_message']" />
      </TabPanel>
    </TabView>
  </div>
</template>
