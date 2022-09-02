import {React, useEffect, useState, forwardRef} from "react"
import AceEditor from "react-ace";
import 'ace-builds/src-noconflict/theme-monokai'
import 'ace-builds/src-noconflict/mode-python'
import "./scriptBox.css"

/**
 * The code blocks wrapper
 * @param {parameter wrapper} props
 * @param {references} ref
 * @return the code block wrapper in html.
 */
const ScriptBox = forwardRef((props, ref)=>{
    {
        const [aceValue, setAceValue] = useState("")
        const [resultFromPython, setResultFromPython] = useState(["",""])
        const [consoleMsg, setConsoleMsg] = useState({msg:"", status: ""})
        var data = {text:aceValue}
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        };
    
        useEffect(()=>{
            props.passData(resultFromPython)
        },[resultFromPython])
        
        useEffect(()=>{
            setAceValue(props.initial)
        },[])

        
        const handleAceChange = (code) =>{
            setAceValue(code)
        }
    
        const handleCodeSubmit = () =>{
            console.log(props.id)
            const url = 'http://127.0.0.1:5000/scriptBox';
            fetch(url, requestOptions
            ).then((response) => {
                var results =  response.json()
                return results
            }).then((response)=>{
                var result = response["result"]
                setConsoleMsg({msg: "Message from code block " + props.id  +" : "+ "\n"+response["terminal"][0], status: response["terminal"][1]})
                setResultFromPython(result)
            })
        }
        ref.current = handleCodeSubmit;
    
        return(                                                                     
            <div className = "InputWrapper">
                <div className="editorWrapper">
                    <div style={{display:"flex"}}>
                        <button className="button-10" onClick={handleCodeSubmit}>
                            submit
                        </button>
                    </div>
                    <div>
                        Block : {" " +props.id}
                    </div>
                    <AceEditor placeholder="code" mode="python" theme="monokai" showPrintMargin={true} showGutter={true} highlightActiveLine={true} fontSize={16}
                        value={aceValue} onChange = {handleAceChange}
                        setOptions={{
                        enableLiveAutocompletion: false,
                        enableSnippets: false,
                        showLineNumbers: true,
                        tabSize: 4,
                        enableBasicAutocompletion: false,
                        }}/>
                    <div classname = 'console'>
                        {consoleMsg["msg"]}
                    </div>
                </div>  
            </div>
        )
    }
})


export default ScriptBox;