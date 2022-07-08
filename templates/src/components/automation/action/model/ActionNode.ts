import Action from "@/model/Action";

class ActionNode {
    $children: ActionNode[];
    children: ActionNode[];
    text: string;
    action: Action;
    isSelected: boolean;

    constructor(action: Action) {
        this.$children = []
        this.children = action.child_action_associations.map(
            child_action_association => new ActionNode(child_action_association.child_action))
        this.text = action.name
        this.action = action
        this.isSelected = false
    }
}

export default ActionNode
