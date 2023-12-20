class Module:
    def __init__(this, type, name, dests):
        this.state = False
        this.type = type
        this.name = name
        this.dests = dests

    def update(this, signal, modules, con_inputs):
        if this.type == '%' and not(signal):
            this.state = not(this.state)
            return this.state
        elif this.type == '&':
            this.state = False
            for input_mod in con_inputs[this.name]:
                if not(modules[input_mod].state):
                    this.state = True
                    return True
            else:
                return False

def main():
    broadcastees = []
    modules = {}
    con_inputs = {}

    with open("20-input.txt", encoding='UTF-8') as file:
        for line in file:
            parts = line.split('->')
            parts[0] = parts[0].strip()
            if parts[0] == 'broadcaster':
                broadcastees = [x.strip() for x in parts[1].strip().split(',')]
                continue
            
            mod_type = parts[0][0]
            mod_name = parts[0][1:]
            mod_dests = [x.strip() for x in parts[1].strip().split(',')]
            modules[mod_name] = Module(mod_type, mod_name, mod_dests)
            if mod_type == '&':
                con_inputs[mod_name] = []
    
    terminator_modules = []
    for mod_name in modules:
        module = modules[mod_name]
        for dest in module.dests:
            if not(dest in modules):
                terminator_modules.append(dest)
    for mod in terminator_modules:
        modules[mod] = Module('t', mod, [])
    for mod_name in modules:
        module = modules[mod_name]
        for dest in module.dests:
            if dest in con_inputs:
                con_inputs[dest].append(mod_name)

    low_pulse_count = 0
    high_pulse_count = 0

    # Array used for part 2
    of_interest = ['xf', 'cm', 'sz', 'gc']
    
    
    for i in range(0, 100000):
        update_queue = [(x, False) for x in broadcastees]
        low_pulse_count += len(broadcastees) + 1

        while len(update_queue) > 0:
            mod_name, val = update_queue.pop(0)

            # Print statement used for part 2
            
            # if mod_name in of_interest and not(val):
            #     print(str(i) + ' ' + mod_name)

            module = modules[mod_name]
            if module.type == 't':
                continue
            if module.update(val, modules, con_inputs):
                high_pulse_count += len(module.dests)
            else:
                low_pulse_count += len(module.dests)
            
            for dest in module.dests:
                dest_module = modules[dest]
                if not(dest_module.type == '%' and module.state):
                    update_queue.append((dest, module.state))
        pass
    
    # Part 1 answer

    print(low_pulse_count * high_pulse_count)
        
    # Part 2 answer:
    # Inspection of the puzzle input reveals that the NAND-gate of interest has four inputs. The commented
    # statements above allow us to find the period of each input going LOW. The LCM of these periods is how
    # many button presses are required to make the output of interest go LOW

            

if __name__ == "__main__":
    main()
