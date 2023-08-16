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
      <TabPanel :header="t('Addresses')">
        <ObjectTable
          :store="mainStore"
          :name="'lotzappAddresses'"
          :default-columns="['user', 'lotzapp_id', 'sync_active']" />
      </TabPanel>
      <TabPanel :header="t('Invoices')">
        <ObjectTable
          :store="mainStore"
          :name="'lotzappInvoices'"
          :default-columns="['invoice', 'lotzapp_id', 'sync_active']" />
      </TabPanel>
    </TabView>
  </div>
</template>
