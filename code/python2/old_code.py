        except Exception, inst:
            type, value, trace = sys.exc_info()

            geom = w.root.geometry()
            list = string.split(geom, '+')
            x = int(list[1]) + 10
            y = int(list[2]) + 10

            tl = w.tl()
            tl.title('Exception')
            tl.geometry('+' + str(x) + '+' + str(y))            
            te = w.te(width=60, height=20)
            w.endfr()

            te.insert(END, str(type) + ':' + str(value))
            te.insert(END, '\n\n')
            tb = extract_tb(trace)
            list = format_list(tb)
            list.reverse()
            for line in list:
                te.insert(END, line)
                te.insert(END, '\n')
            del trace
            
        
