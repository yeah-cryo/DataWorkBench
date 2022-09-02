import {React,useState, useRef} from "react"
import "./wrapper.css"
import SpreadSheet from "./spreadSheet";
import ScriptBox from "./scriptBox"

/**
 * The wrapper that wraps both code blocks and spreadsheets
 * @return the html of wrapper that contains code blocks and spreadsheets
 */
function Wrapper() {
    const [numBlock, setNumBlock] = useState(1)
    const [grid, setgrid] = useState([[],[]])
    const [currentSheet, setSheet] = useState("")
    const chilRef =  Array(numBlock).fill(useRef())
    const [Python, setPython] = useState({})

    var sheet_names = Object.keys(grid)

    return(
        <div className = "WorkFlowWrapper">
            <div className  = "sheetBar">
                <span>select sheet</span>
                {sheet_names.map((e)=>{
                    return <button className="sheetButton" onClick={(e)=>{setSheet(e.target.value)}} value ={e}>{e}</button>
                })}
            </div>
            <div className = "displayArea">
                <SpreadSheet  passPy = {str => {var obj = Python; obj[numBlock] = str  ;setPython(obj);}} data= {grid} sheet = {currentSheet} />
            </div>
            <div className = "dividingStick">
            </div>
            <div className = "inputArea">
                <button  button class="button-64" role="button" onClick={()=>{setNumBlock(numBlock+1);}}><span class="text">add code block</span></button>
                <div className = "userInput">
                    <div classname = 'box' >
                        {Array(numBlock).fill("1").map((e, i)=>{
                            return(
                            <div style={{padding: "12px"}}>
                                <ScriptBox  ref = { chilRef} passData = {c => {setgrid( c)}} id = {i} initial = {Object.keys(Python).includes(i.toString()) ? Python[i.toString()] : ""}/> 
                            </div>
                            )
                        })}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Wrapper;