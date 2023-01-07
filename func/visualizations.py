import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def vis4(count,G_original,G,heroA='CAPTAIN AMERICA',heroB='IRON MAN/TONY STARK'):
    print('Number of edges to be removed: ', count,'\n')
    
    color_map = ['red' if node==heroA else 'green' if node==heroB else 'grey' for node in G]
            
    fig1,ax = plt.subplots()
    fig1.suptitle('Original Graph')
    handles = [plt.plot([], marker="o", ls="", color=c)[0] for c in ['red','green','grey']]
    labels = [f'{heroA}', f"{heroB}", 'other heroes']
    plt.legend(handles, labels)
    nx.draw_networkx(G_original,with_labels= False,node_color=color_map,node_size=50,alpha=1)
    
    fig2,ax = plt.subplots()
    fig2.suptitle('Disconnected Graphs')
    nx.draw_networkx(G,with_labels= False,node_color=color_map,node_size=50,alpha=1)
    plt.legend(handles, labels)
    plt.show()
    return

def vis5(communities, count,G_new,G, heroA = 'CAPTAIN AMERICA', heroB = 'IRON MAN/TONY STARK'):
    k = len(communities)
    v = heroA
    u = heroB
    
    node_groups = []
    mydict = {}
    colors = ['blue','red']
    for i in range(k):
        node_groups.append(communities[i])
        mydict[f'Community{i+1}'] = list(communities[i])
        colors.append(plt.cm.Set2(i+2))
    
    color_map = []
    for node in G:
        if node == v:
            color_map.append('blue')
        elif node == u:
            color_map.append('red')
        else:
            for i in range(k):
                if node in node_groups[i]:
                    color_map.append(plt.cm.Set2(i+2)) 
                    
    
            
    print('Number of edges to remove: ', count, '\n')
            
    table = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in mydict.items() ]))
    
    '''if len(table[table['red']==u])== len(table[table['red']==v]):
        print(f'The two heroes, {u} and {v}, are on the same community.\n')
    else:
        print(f'The two heroes, {u} and {v}, are not on the same community.\n')'''
    
    print('\n',table,'\n')
    
    
    fig1,ax = plt.subplots()
    fig1.suptitle('Original Graph')
    nx.draw_networkx(G,with_labels= False,node_size=50,alpha=0.8)
    
    
    
    fig2,ax = plt.subplots()
    fig2.suptitle('Communities Graph')
    handles = [plt.plot([], marker="o", ls="", color=c)[0] for c in colors]
    labels = [f'{v}',f'{u}']
    for i in range(k):
        labels.append(f'community{i+1}') 
        
    plt.legend(handles, labels)
    nx.draw_networkx(G, node_color=color_map, with_labels=False,node_size=50,alpha=0.8)
    
    
    fig3,ax = plt.subplots()
    fig3.suptitle('Final Graph')
    nx.draw_networkx(G_new, node_color=color_map, with_labels=False,node_size=50,alpha=0.8)
    plt.legend(handles, labels)
    plt.show()
    

    return 
