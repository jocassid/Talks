import org.python.core.PyException;
import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.util.PythonInterpreter;

public class EmbeddedUsingMyModule
{
    public static void main(String[] args) throws PyException
    {
        PythonInterpreter interp = new PythonInterpreter();
        interp.exec("import my_module");
        interp.exec("my_module.myFunction()");
        interp.exec("myClass = my_module.MyClass()");
        interp.exec("myClass.method()");
        interp.exec("for i in range(10):\n\tprint(i)");
        
        
    }
}


