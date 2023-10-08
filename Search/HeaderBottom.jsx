import React, { useEffect, useState } from "react";
import { FaSearch } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./headerbottom.scss";

const HeaderBottom = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [showSearchBar, setShowSearchBar] = useState(false);
  const navigate = useNavigate();
  const [data, setData] = useState([]);

  const handleSearch = (e) => {
    setSearchQuery(e.target.value);
    setShowSearchBar(true);
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get(
          process.env.REACT_APP_API_URL + `/products?populate=*`,
          {
            headers: {
              Authorization: "bearer " + process.env.REACT_APP_API_TOKEN,
            },
          }
        );
        setData(res.data.data);
      } catch (err) {
        console.log(err);
      }
    };
    fetchData();
  }, []);
  const filteredData = data.filter((item) => {
    const lowerCaseTitle = item.attributes.title.toLowerCase();
    const lowerCaseSearchQuery = searchQuery.toLowerCase();
    return lowerCaseTitle.includes(lowerCaseSearchQuery);
  });

  return (
    <div className="search-main">
      <div className={`search ${showSearchBar ? "search-open" : ""}`}>
        <>
          <div className="search_icon">
            <FaSearch />
          </div>
          <input
            className="search_input"
            type="text"
            onChange={handleSearch}
            value={searchQuery}
            placeholder="Tìm kiếm"
          />
          <div className="search_results">
            {searchQuery &&
              filteredData.map((item) => (
                <div
                  onClick={() =>
                    navigate(`/product/${item.id}`, {
                      state: {
                        item: item,
                      },
                    }) &
                    setShowSearchBar(false) &
                    setSearchQuery("")
                  }
                  key={item.id}
                  className="search_result"
                >
                  <img
                    src={
                      process.env.REACT_APP_UPLOAD_URL +
                      item.attributes.img.data?.attributes.url
                    }
                    alt=""
                    className="zxczxcz"
                    style={{ width: "50px", height: "50px" }}
                  />
                  <div className="search_result-info">
                    <p className="search_result-title">
                      {item.attributes.title}
                    </p>
                    <p className="search_result-price">
                      Price:{" "}
                      <span className="search_result-price-value">
                        ${item.attributes.price}
                      </span>
                    </p>
                  </div>
                </div>
              ))}
          </div>
        </>
      </div>
    </div>
  );
};

export default HeaderBottom;
