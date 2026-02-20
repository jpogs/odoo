/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";

patch(Order.prototype, {

    setup() {
        super.setup(...arguments);
        if (!this.table_start_time) {
            this.table_start_time = new Date().toISOString();
        }
    },

    export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.table_start_time = this.table_start_time;
        json.table_end_time = new Date().toISOString();
        return json;
    },

    getTableDurationSeconds() {
        if (!this.table_start_time) return 0;
        const start = new Date(this.table_start_time);
        const now = new Date();
        return Math.floor((now - start) / 1000);
    },
});
