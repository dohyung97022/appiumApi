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
      <div class="col-4 m-auto">name</div>
      <div class="col-3 m-auto">run</div>
      <div class="col-4 m-auto">edit</div>
      <div class="col-1">
        <button class="btn btn-primary" v-on:click="add_phone_action_row">
          <font-awesome-icon icon="plus"/>
        </button>
      </div>
    </div>

    <hr/>

    <draggable :list="actionRowList" item-key="id">
      <template #item="{ element, index }">
        <div class="row text-center mb-3">

          <!--        name        -->
          <div class="col-4">
            <input type="text" class="form-control" v-model="element.name">
          </div>

          <!--        run        -->
          <div class="dropdown col-3">
            <button class="btn btn-light" v-on:click="test">
              <font-awesome-icon icon="play"/>
            </button>
          </div>

          <!--        edit        -->
          <div class="col-4">
            <button class="btn btn-light" v-on:click="test">
              <font-awesome-icon icon="pen-to-square"/>
            </button>
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
import Action from "@/model/Action";
import ActionRow from "@/components/automation/phoneAction/model/ActionRow";

export default defineComponent({
  name: "AutomationPhoneActionList",

  components: {
    draggable
  },

  data() {
    return {
      actionRowId : 0,
      actionRowList: [],
      getActionsParameters: {
        udid: 'test1'
      }
    }
  },

  methods: {

    /**
     * action
     */
    get_phone_actions() {
      axios.get('http://127.0.0.1:8082/api/automation/actions', {params : this.getActionsParameters})
           .then(res => {console.log(res)})
           .catch(err => {console.log(err)})
    },

    save_phone_actions() {
      axios.post('http://127.0.0.1:8082/api/automation/action/action', null)
           .then(res => {console.log(res)})
           .catch(error => (console.log(error)))
    },

    add_phone_action_row() {
      const newAction = new Action('');
      const newActionRow = new ActionRow(newAction, this.actionRowId)

      this.actionRowList.push(newActionRow);
      this.actionRowId++
    },

    remove_phone_action_row(index) {
      this.actionRowList.splice(index, 1);
    },

    test() {
      console.log('test')
    }
  }
})
</script>

<style scoped>
</style>