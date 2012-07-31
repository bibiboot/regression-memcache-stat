from pylab import *

"""
Create graph images from the data using pylab
"""

def main():   
    #my_dict = {'A': 70, 'B': 290, 'C': 130}
    hit = datasource()

    bar_graph(hit, graph_title='Advanceperiod vs Hit', output_name="Hit.png")

def bar_graph(name_value_dict, graph_title='', output_name='bargraph.png'):
    figure(figsize=(28, 6)) # image dimensions   
    title(graph_title, size='x-small')
    
    # add bars
    for i, key in zip(range(len(name_value_dict)), name_value_dict.keys()):
        bar(i + 0.25 , name_value_dict[key], color='red')
    
    # axis setup
    xticks(arange(0.65, len(name_value_dict)), 
                  [('%s' % (name)) for name, value in zip(name_value_dict.keys(), name_value_dict.values())], 
                  size='xx-small')

    #max_value = max(name_value_dict.values())
    max_value = 100
    tick_range = arange(0, max_value, (max_value / 10))

    yticks(tick_range, size='xx-small')

    formatter = FixedFormatter([str(x) for x in tick_range])

    gca().yaxis.set_major_formatter(formatter)
    gca().yaxis.grid(which='major') 
    
    savefig(output_name)

def datasource():
    hit = {}
    data_list = []
    with open('test.txt','r') as f:
        data_list = eval(f.readlines()[0])

    for data_dict in data_list[:100]:
        adv = int(data_dict['_id']['advanceperiod'])
        hits = int(data_dict['value']['hit'])
        hit[adv] = hits
    return hit

if __name__ == "__main__":
    main()
