import Action from "@/components/automation/action/model/Action";

class ActionNode {
    $children: ActionNode[];
    text: string;
    action: Action;
    isSelected: boolean;

    constructor(action: Action) {
        this.$children = action.child_actions.map(action => new ActionNode(action))
        this.text = action.name
        this.action = action
        this.isSelected = false
    }
}

export default ActionNode
