import { Component } from "react";
import { useParams } from "react-router-dom";

class Details extends Component {
    render() {
        const { name, lastName } = this.props;
        
        return (
            <h1>Welcome to details page of: {name}</h1>
        );
    }
}

const DetailsWrapper = () => {
    let { name } = useParams();
    return <Details name={name} />;
};

export default DetailsWrapper;