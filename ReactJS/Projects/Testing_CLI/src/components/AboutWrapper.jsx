import { useNavigate } from "react-router-dom";
import About from "./About";

export default function AboutWrapper() {
    const navigate = useNavigate();
    return <About navigate={navigate} />;
}
