import Macro from "@/components/automation/action/model/Macro";

export class MacroRow {
    id: number;
    name: string;
    macro: Macro;

    constructor(macro: Macro, id: number) {
        this.id = id
        this.name = macro.name
        this.macro = macro
    }

    toMacro() {
        this.macro.name = this.name
        return this.macro
    }
}

export default MacroRow
