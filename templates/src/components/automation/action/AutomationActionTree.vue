<template>
  <div class="row row-cols-2 justify-content-between">
    <!--     행동절차     -->
    <div class="col-3">
      <Draggable :treeData="treeData" :ondragend="onDragEnd" idKey="id" parentIdKey="pid">
        <template v-slot="{ node, tree }">

          <template v-if="node.$level === 1">
            <div class="mb-1 d-flex justify-content-between row">
              <h4 class="col-10">행동절차</h4>

              <div class="col-2 p-0 text-center">
                <button class="btn btn-primary" v-on:click="save_action_tree(node, tree)">
                  <font-awesome-icon icon="floppy-disk"/>
                </button>
              </div>
            </div>

            <div class="mb-3 d-flex justify-content-between row">
              <div class="col-10">
                <input type="text" class="form-control" v-model="addActionName">
              </div>
              <div class="col-2 p-0 text-center">
                <button class="btn btn-primary" v-on:click="add_action(tree)">
                  <font-awesome-icon icon="plus"/>
                </button>
              </div>
            </div>
            <hr/>
          </template>

          <div class="mb-3 d-flex justify-content-between">
            <h5 class="mb-auto mt-auto" v-bind:style="[node.isSelected ? {'color':'red'} : '']"
                v-on:click="select_action(node, tree)"> • {{ node.text }}</h5>

            <button v-bind:style="[node.$level !== 1 ? '' : {'visibility':'hidden'}]"
                    class="btn btn-light" v-on:click="remove_action(node, tree)">
              <font-awesome-icon icon="minus"/>
            </button>
          </div>

        </template>
      </Draggable>

      <hr/>

    </div>
    <!--     매크로 리스트     -->
    <div class="col-8">
      <div class="row text-center mb-1">
        <h4 class="col-11 text-start">매크로 리스트</h4>
        <div class="col-1">
          <button class="btn btn-primary" v-on:click="save_macro_list">
            <font-awesome-icon icon="floppy-disk"/>
          </button>
        </div>
      </div>
      <div class="row text-center">
        <div class="col-2 m-auto">name</div>
        <div class="col-2 m-auto">macroType</div>
        <div class="col-4 m-auto">element</div>
        <div class="col-1 m-auto">index</div>
        <div class="col-2 m-auto">wait</div>
        <div class="col-1">
          <button class="btn btn-primary" v-on:click="add_macro">
            <font-awesome-icon icon="plus"/>
          </button>
        </div>
      </div>

      <hr/>

      <draggable :list="macroRowList" item-key="id">
        <template #item="{ element, index }">
          <div class="row text-center">

            <!--        title        -->
            <div class="col-2">
              <input type="text" class="form-control" v-model="element.name">
            </div>

            <!--        macroType        -->
            <div class="dropdown col-2">
              <select class="form-select mb-3" aria-label=".form-select-lg" v-model="element.macro.macro_type">
                <option value="CLICK">CLICK</option>
                <option value="DRAG">DRAG</option>
                <option value="SCROLL">SCROLL</option>
                <option value="RUN">RUN</option>
              </select>
            </div>

            <!--        element        -->
            <div class="col-4">
              <div class="input-group w-100">

                <select class="form-select" style="width: 40%;" aria-label=".form-select-lg"
                        v-model="element.macro.element_type">
                  <option value="ID">ID</option>
                  <option value="XPATH">XPATH</option>
                  <option value="LINK_TEXT">LINK_TEXT</option>
                  <option value="PARTIAL_LINK_TEXT">PARTIAL_LINK_TEXT</option>
                  <option value="NAME">NAME</option>
                  <option value="TAG_NAME">TAG_NAME</option>
                  <option value="CLASS_NAME">CLASS_NAME</option>
                  <option value="CSS_SELECTOR">CSS_SELECTOR</option>
                </select>

                <input type="text" class="form-control" style="width: 60%;" v-model="element.macro.element">
              </div>
            </div>

            <!--        index        -->
            <div class="col-1">
              <input type="number" class="form-control text-center" v-model="element.macro.macro_index">
            </div>

            <!--        wait        -->
            <div class="col-2">
              <div class="input-group">
                <input type="number" class="form-control" v-model="element.macro.min_wait_sec">
                <span class="input-group-text">~</span>
                <input type="number" class="form-control" v-model="element.macro.max_wait_sec">
              </div>
            </div>

            <!--       delete        -->
            <div class="col-1">
              <button class="btn btn-light" v-on:click="remove_macro(index)">
                <font-awesome-icon icon="minus"/>
              </button>
            </div>
          </div>
        </template>
      </draggable>

      <hr class="m-0"/>

    </div>
  </div>

</template>

<script>
import {defineComponent} from "vue";
import Action from "@/components/automation/action/model/Action";
import axios from "axios";
import {Draggable} from '@he-tree/vue3'
import ActionNode from "@/components/automation/action/model/ActionNode";
import Macro from "@/components/automation/action/model/Macro";
import draggable from "vuedraggable";
import MacroRow from "@/components/automation/action/model/MacroRow";

export default defineComponent({
  name: "AutomationActionTree",

  components: {
    Draggable, draggable
  },

  data() {
    return {
      queryActionSeq: 1,
      addActionName: '',
      selectedActionNode: null,
      treeData: [],
      macroRowList: [],
      macroRowId: 0
    }
  },

  async created() {
    this.get_action();
  },

  methods: {

    /**
     * action
     */
    get_action() {
      axios.get('http://127.0.0.1:8082/api/automation/action/' + this.queryActionSeq)
          .then(res => {
            this.treeData = [new ActionNode(res.data)]
          })
          .catch(error => (console.log(error)))
    },

    select_action(node, tree) {
      this.macroRowList = node.action.macros.map(macro => new MacroRow(macro, this.macroRowId++))
      tree.nodes.forEach(function (node) {
        node.isSelected = false
      })
      node.isSelected = true
      this.selectedActionNode = node;
    },

    add_action(tree) {
      const node = new ActionNode(new Action(this.addActionName))
      tree.addNode(node, tree.nodes[0].$id)
      this.addActionName = ''
    },

    remove_action(node, tree) {
      tree.removeNode(node)
    },

    save_action_tree(tree) {
      const action = Action.ofActionNode(tree)

      axios.post('http://127.0.0.1:8082/api/automation/action/action', action)
           .then(res => {console.log(res)})
           .catch(error => (console.log(error)))
    },

    /**
     * macro
     */
    add_macro() {
      if (this.selectedActionNode === null) {
        alert("행동절차를 선택해주세요.")
        return
      }

      const selectedActionSeq = this.selectedActionNode.action.action_seq
      const newMacro = new Macro(selectedActionSeq);
      const newMacroRow = new MacroRow(newMacro, this.macroRowId)

      this.macroRowList.push(newMacroRow);
      this.macroRowId++
    },

    remove_macro(index) {
      this.macroRowList.splice(index, 1);
    },

    set_macro_order() {
      let i = 0;
      this.macroRowList.forEach(value => value.macro.macro_order = i++)
    },

    convert_selected_to_macros() {
      return this.macroRowList.map(value => value.toMacro());
    },

    save_macro_list() {
      if (this.selectedActionNode === null) {
        alert("행동절차를 선택해주세요.")
        return
      }
      this.set_macro_order()
      const action = Action.ofActionNode(this.selectedActionNode)
      action.macros = this.convert_selected_to_macros()

      axios.post('http://127.0.0.1:8082/api/automation/action/macro', action)
           .then(res => {console.log(res)})
           .catch(error => (console.log(error)))
    },

    /**
     * 1 level 이하 tree node 불가능
     */
    onDragEnd(store) {

      function isNotMinLevel(minLevel, store) {
        if (store.placeholderLevel === minLevel) {
          return false
        }
      }

      return isNotMinLevel(1, store)
    }
  }
})
</script>

<style scoped>
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>