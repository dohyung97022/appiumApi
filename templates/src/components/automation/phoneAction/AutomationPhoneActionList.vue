<template>
  <div class="col">
    <!--     행동 리스트     -->
    <div class="row text-center mb-1">
      <h4 class="col-11 text-start">행동 리스트</h4>
      <div class="col-1">
        <button class="btn btn-primary" v-on:click="save_phone_actions">
          <font-awesome-icon icon="floppy-disk"/>
        </button>
      </div>
    </div>
    <div class="row text-center">
      <div class="col-2 m-auto">name</div>
      <div class="col-2 m-auto">run</div>
      <div class="col-2 m-auto">edit</div>
      <div class="col-3 m-auto">loopType</div>
      <div class="col-2 m-auto">loop</div>
      <div class="col-1">
        <button class="btn btn-primary" v-on:click="add_phone_action_row">
          <font-awesome-icon icon="plus"/>
        </button>
      </div>
    </div>

    <hr/>

    <draggable :list="phoneActionRowList" item-key="id">
      <template #item="{ element, index }">
        <div class="row text-center">

          <!--        name        -->
          <div class="col-2">
            <input type="text" class="form-control" v-model="element.phoneActionAssociation.action.name">
          </div>

          <!--        run        -->
          <div class="dropdown col-2">
            <button class="btn btn-light" v-on:click="run_action(element)">
              <font-awesome-icon icon="play"/>
            </button>
          </div>

          <!--        edit        -->
          <div class="col-2">
              <button @click="edit_action(element)" class="btn btn-light">
                <font-awesome-icon icon="pen-to-square"/>
              </button>
          </div>

          <!--        loopType        -->
          <div class="dropdown col-3">
            <select class="form-select mb-3" aria-label=".form-select-lg" v-model="element.phoneActionAssociation.loop_type">
              <option value="DAILY">DAILY</option>
              <option value="SINGLE_USE">SINGLE_USE</option>
            </select>
          </div>

          <!--        loop        -->
          <div class="col-2">
            <input type="number" class="form-control" v-model="element.phoneActionAssociation.loop">
          </div>

          <!--       delete        -->
          <div class="col-1">
            <button class="btn btn-light" v-on:click="remove_phone_action_row(index)">
              <font-awesome-icon icon="minus"/>
            </button>
          </div>
        </div>
      </template>
    </draggable>

    <hr class="m-0"/>

  </div>

</template>

<script>
import {defineComponent} from "vue";
import axios from "axios";
import draggable from "vuedraggable";
import PhoneActionRow from "@/components/automation/phoneAction/model/PhoneActionRow";
import Phone from "@/model/Phone";
import PhoneActionAssociation from "@/model/PhoneActionAssociation";

export default defineComponent({
  name: "AutomationPhoneActionList",

  components: {
    draggable
  },

  data() {
    return {
      udid: this.$route.query.udid,
      actionRowId : 0,
      phoneActionRowList: [],
      getPhoneActionsParameters: {
        udid: ''
      },
      savePhoneActionsParameters: {
        udid: '',
        phoneActionAssociation: []
      },
      runPhoneActionParameters: {
        udid: '',
        actionSeq: null
      }
    }
  },

  async created() {
    this.get_phone_actions()
  },

  methods: {

    /**
     * phone action
     */
    get_phone_actions() {
      this.getPhoneActionsParameters.udid = this.udid

      axios.get('http://127.0.0.1:8082/api/automation/phone/actions', {params : this.getPhoneActionsParameters})
           .then(res => {
             this.phoneActionRowList = new Phone(res.data).action_associations
                 .map(association => new PhoneActionRow(this.actionRowId++, association))
           })
           .catch(err => {console.log(err)})
    },

    save_phone_actions() {
      this.savePhoneActionsParameters.udid = this.udid
      this.savePhoneActionsParameters.phoneActionAssociation = this.phoneActionRowList.map(phoneActionRow => phoneActionRow.phoneActionAssociation)

      axios.post('http://127.0.0.1:8082/api/automation/phone/actions', this.savePhoneActionsParameters)
           .then(res => {this.get_phone_actions(); alert('저장되었습니다.'); console.log(res);})
           .catch(error => (console.log(error)))
    },

    add_phone_action_row() {
      const phoneActionAssociation = new PhoneActionAssociation();
      phoneActionAssociation.action.is_root = true

      this.phoneActionRowList.push(new PhoneActionRow(this.actionRowId, phoneActionAssociation));
      this.actionRowId++
    },

    remove_phone_action_row(index) {
      this.phoneActionRowList.splice(index, 1);
    },

    edit_action(phoneActionRow) {
      if (phoneActionRow.phoneActionAssociation.action_seq === null) {
        alert('저장 이후에 편집이 가능합니다.')
        return;
      }
      this.$router.push('/automation/action?actionSeq=' + phoneActionRow.phoneActionAssociation.action_seq + '&udid=' + this.udid)
    },

    run_action(phoneActionRow) {
      if (phoneActionRow.phoneActionAssociation.action_seq === null) {
        alert('저장 이후에 실행이 가능합니다.')
        return;
      }

      this.runPhoneActionParameters.actionSeq = phoneActionRow.phoneActionAssociation.action_seq
      this.runPhoneActionParameters.udid = this.udid

      axios.get('http://127.0.0.1:8082/api/automation/phone/action/appium/run', {params : this.runPhoneActionParameters})
          .then(res => {console.log(res)})
          .catch(error => (console.log(error)))
    },

    test() {
      console.log('test')
    }
  }
})
</script>

<style scoped>
</style>